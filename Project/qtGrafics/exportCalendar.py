import psycopg2
import db.handler.meetings_maagement as meetings
import db.handler.personsManagement as person
from icalendar import Calendar, Event
import pytz

class ExportCalendar():
    """
    A class that helps me export from my database informations about meetings
    to a .ics file
    
    ...

    Atributes
    ---------
    meetings : class
        A class that have meeting management functions for atributes of my database
    username : str
        A string that is initialised from constructor and that we use to know the user that imports
    person : class
        A class that have functions which manage user data in our data base
    idUser : Integer
        An integer that represents my user ID
    
    Methods
    -------
    def OpenFile():
        This method shows a window where I can chose the path for importing the file

    def Export():
        Is a function that use a meeting management object and a user data management object  
        which helps me to get all meetings data or invites data and the write(export) them in
        an .ics file.
    """

    def __init__(self,username):
        """
        Initialise all the necessary attributes for the export calendar object.

        Parameters
        ----------
        username : str
        It represents the username that want to export the necessary data to a chosen ics file.
        """

        self.meetings = None
        self.username = username
        self.person = None
        self.idUser = None

    def Export(self):
        """
        This function has the role to take all neccesary data for exporting in a file that is a 
        calendary format .ics file.The data is taken wit meeting management object and person 
        management object from specific tabels of my database

        Parameters
        ----------
        """            

        self.meetings = meetings.MeetingManagement()
        cal = Calendar()
        self.person = person.PersonManagement()
        self.idUser = self.person.getUserId(self.username)
        rows_meetInvited = self.meetings.getInvitations(self.username)
        rows_meetHost = self.meetings.selectMeetsByUserId(self.idUser)
        
        for row in rows_meetHost:
            event = Event()
            event.add('summary', f'Meeting ID: {row[0]} (Host), User ID: {self.idUser}')
            event.add('dtstart', row[1].replace(tzinfo=pytz.utc))
            event.add('dtend', row[2].replace(tzinfo=pytz.utc))
            cal.add_component(event)

        for row in rows_meetInvited:
            event = Event()
            event.add('summary', f'Meeting ID: {row[0]} (Invited), User ID: {self.idUser}')
            event.add('dtstart', row[1].replace(tzinfo=pytz.utc))
            event.add('dtend', row[2].replace(tzinfo=pytz.utc))
            cal.add_component(event)

        with open(f"/home/lolluckestar/Desktop/Anul III/Sem I/Python/Lab/Python/Project/exports/meetingAppointments_{self.username}.ics", "wb") as f:
            f.write(cal.to_ical())

        print("Calendarul a fost salvat ca 'meeting_appointments.ics'")