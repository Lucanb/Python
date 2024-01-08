import psycopg2
import db.handler.meetings_maagement as meetings
import db.handler.personsManagement as person
from icalendar import Calendar, Event
import tkinter as tk
from tkinter import filedialog
import pytz
from io import StringIO

class ImportCalendar():
    
    def __init__(self,username):
        self.meetings = None
        self.username = username
        self.person = None
        self.idUser = None
        self.filePath = None
    
    def OpenFile(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        self.filePath = file_path

    def parseFile(self):
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

