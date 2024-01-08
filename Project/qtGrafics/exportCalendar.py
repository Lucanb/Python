import psycopg2
import db.handler.meetings_maagement as meetings
import db.handler.personsManagement as person
from icalendar import Calendar, Event
import pytz

class ExportCalendar():
    
    def __init__(self,username):
        self.meetings = None
        self.username = username
        self.person = None
        self.idUser = None

    def Export(self):

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