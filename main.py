from SessionManager.Session import Session

# Define Required Variables
username=''
password=''
charID = '' # You can get this when hovering over character name after login screen.

# Create Session
s = Session(username,password,charID)

# Run Login to Establish Session
s.Login()

# Start Bot
s.Start()