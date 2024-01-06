
selectIdMeet = "SELECT * FROM meetingAppointments WHERE hostId = %s"
selectAllMeets = "SELECT * FROM meetingAppointments WHERE hour_begin >= %s AND hour_end <= %s"
addMeet = "INSERT INTO meetingAppointments (hostId, hour_begin, hour_end) VALUES (%s, %s, %s) RETURNING meetingId"
deleteInviteID = "DELETE FROM invitations WHERE personId = %s"
deleteMeetID = "DELETE FROM meetingAppointments WHERE meetingId = %s"
deleteInviteMeetIDpersonID = "DELETE FROM invitations WHERE personId = %s AND meetingId = %s"
allPersonInvites = """
    SELECT i.* FROM invitations i
    JOIN personData p ON i.personId = p.personId
    WHERE p.nume = %s OR p.prenume = %s
"""
allMeetInvites = """
    SELECT i.* FROM invitations i
    JOIN meetingAppointments m ON i.meetingId = m.meetingId
    WHERE m.hour_begin <= %s AND m.hour_end >= %s
"""