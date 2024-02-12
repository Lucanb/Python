import psycopg2
import db.handler.meetings_maagement as meetings
import db.handler.personsManagement as person
from icalendar import Calendar, Event
import tkinter as tk
from tkinter import filedialog
import pytz
from io import StringIO

class ImportCalendar():
    """
    A class that helps me importing in my database informations about meetings
    from a .ics file
    
    ...

    Atributes
    ---------
    meetings : class
        A class that have meeting management functions for atributes of my database
    username : str
        A string that is initialised from constructor and that we use to know the user that imports
    person : class
        A class that have functions which manage user data in our data base
    filePath : str
        A string that is chosen when I use import button, it represents the path to file which I want to import
    
    Methods
    -------
    def OpenFile():
        This method shows a window where I can chose the path for importing the file
    def parseFile():
        Is a method that helps me to parse elements from the file that I want to imports
    def Import():
        Is a function that use parseFile to parse the file,OpenFile to have a path and then
        it imports those data from that file to my database in a tabel after 2 types : Host
        and Invited.It verify if those data were inserted before --> in that case it will
        not isert them again.
    """

    def __init__(self,username):
        """
        Initialise all the necessary attributes for the import calendar object.

        Parameters
        ----------
        username : str
        It represents the username that want to import the data from a chosen ics file.
        """

        self.meetings = None
        self.username = username
        self.person = None
        # self.idUser = None
        self.filePath = None
    
    def OpenFile(self):
        """
        Initialise all the necessary attributes for the import calendar object object.

        Parameters
        ----------
        username : str
        It represents the username that want to import the data from a chose ics file.
        """

        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        self.filePath = file_path

    def parseFile(self):
        """
        This function is for parsing the data from a specific file.

        Parameters
        ----------
        """    

        with open(self.filePath, 'r') as f:
            calendar = Calendar.from_ical(f.read())
        for element in calendar.walk():
            if element.name == "VEVENT":
                summary = str(element.get('summary'))
                details = summary.split(", ")
                meetingId = details[0].split(":")[1].strip().split(" ")[0]
                userId = details[1].split(":")[1].strip()
                userRole = "Host" if "(Host)" in summary else "Invited"
                begin_hour = element.get('dtstart').dt.replace(tzinfo=pytz.utc)
                end_hour = element.get('dtend').dt.replace(tzinfo=pytz.utc)
                yield {
                    'meetingid': meetingId,
                    'userid': userId,
                    'role': userRole,
                    'start': begin_hour,
                    'end': end_hour
                }

    def Import(self):
        """
        This function parse a file and then it verify if the data from those file exists
        in specific table,if they don't it will be inserted in tabels.

        Parameters
        ----------
        """    
        
        self.meetings = meetings.MeetingManagement()
        self.person = person.PersonManagement()

        for event in self.parseFile():
            meeting_id = event['meetingid']
            user_id = event['userid']
            role = event['role']
            start = event['start']
            end = event['end']

            if role == "Host":
                if not self.meetings.meetingExists(meeting_id, user_id):
                    print(user_id)
                    self.meetings.createMeetImport(meeting_id,user_id, start, end)
                else:
                    print('Deja exista acest meet')
            else: 
                if not self.meetings.invitationExists(meeting_id, user_id):
                    self.meetings.createInvitation(meeting_id, user_id)
                else:
                    print('Deja exista acest meet')
        print("Importul datelor din calendar a fost finalizat.")

