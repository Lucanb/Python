
loginUser  = "SELECT * FROM accountusers WHERE username = %s AND password = %s"
createUser = "INSERT INTO accountusers (username, password) VALUES (%s, %s)"
existsUsers = "SELECT * FROM accountusers WHERE username = %s"