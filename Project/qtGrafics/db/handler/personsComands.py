
deleteInvPersonId = "DELETE FROM invitations WHERE personid = %s"
deleteMeetPersonId = "DELETE FROM meetingappoinments WHERE hostid = %s"
deleteUserData = "DELETE FROM persondata WHERE personid = %s"
deleteAccount = "DELETE FROM accountusers WHERE userid = %s"
insertAccounts = "INSERT INTO accountusers (username, password) VALUES (%s, %s) RETURNING id"
insertUserData = "INSERT INTO persondata (personid, nume, prenume) VALUES (%s, %s, %s)"
UpdateUserData = "UPDATE persondata SET nume = %s, prenume = %s WHERE personid = %s"
allPersonsAfterData = "SELECT * FROM persondata WHERE nume = %s OR prenume = %s"