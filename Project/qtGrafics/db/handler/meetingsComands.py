
selectIdMeet = "SELECT * FROM meetingAppointments WHERE hostId = %s"
selectAllMeets = "SELECT * FROM meetingAppointments WHERE hour_begin >= %s AND hour_end <= %s"
addMeet = "INSERT INTO meetingappointments (hostId, hour_begin, hour_end) VALUES (%s, %s, %s) RETURNING meetingid"
deleteInviteID = "DELETE FROM invitations WHERE personId = %s"
deleteMeetID = "DELETE FROM meetingAppointments WHERE meetingId = %s"
deleteInviteMeetIDpersonID = "DELETE FROM invitations WHERE personid = %s AND meetingid = %s"
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
allMeetInvById = """
SELECT m.meetingid, m.hour_begin, m.hour_end FROM meetingappointments m
JOIN invitations i ON m.meetingid = i.meetingid
WHERE i.personid = %s
UNION
SELECT m.meetingid, m.hour_begin, m.hour_end FROM meetingappointments m
WHERE m.hostid = %s
"""
addInvite = "INSERT INTO invitations (meetingid, personid) VALUES (%s, %s)"
InvitationByNameAndIdMeet = "SELECT * FROM invitations WHERE meetingid = %s AND personid = %s"
getMeetAfterId = "SELECT * FROM meetingAppointments WHERE meetingid = %s"
getMeetYouInvited = """
SELECT m.meetingid, m.hour_begin, m.hour_end
FROM invitations i
JOIN meetingappointments m ON i.meetingid = m.meetingid
JOIN accountusers u ON i.personid = u.userid
WHERE u.username = %s
"""
selectIdMeetV = "SELECT meetingid, hour_begin, hour_end FROM meetingAppointments WHERE hostId = %s"
meetExists = "SELECT * FROM meetingAppointments WHERE meetingid = %s AND hostid = %s"
invitationExists = "SELECT * FROM invitations WHERE meetingid = %s AND personid = %s"
addMeetV = "INSERT INTO meetingappointments (meetingid,hostId, hour_begin, hour_end) VALUES (%s, %s, %s, %s) RETURNING meetingid"
existsMeetID = "SELECT * FROM meetingAppointments WHERE meetingid = %s"
deleteInvMeetID = "DELETE FROM invitations WHERE meetingid = %s"
searchInvitationIdUSer = "SELECT * FROM invitations WHERE personid = %s"