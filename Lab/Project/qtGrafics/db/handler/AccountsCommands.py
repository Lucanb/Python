
loginUser  = "SELECT * FROM accountusers WHERE username = %s AND password = %s"
createUser = "INSERT INTO accountusers (username, password) VALUES (%s, %s) RETURNING userid"
existsUsers = "SELECT * FROM accountusers WHERE username = %s"
addPerson = "INSERT INTO persondata (personid,username, prenume, nume) VALUES (%s,%s, %s, %s)"