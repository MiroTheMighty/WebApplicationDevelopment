#!C:\Users\Miro\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
email = form.getvalue('email')
country = form.getvalue('country')
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
username = form.getvalue('username')
password = form.getvalue('password')

print(f"""
<!DOCTYPE html>
<html lang="en">
      
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registration Summary</title>
    </head>
      
    <body>
        <h1>Registration Summary</h1>
        <p>Email: {email}</p>
        <p>Country: {country}</p>
        <p>First Name: {first_name}</p>
        <p>Last Name: {last_name}</p>
        <p>Username: {username}</p>
        <p>Password: {password}</p>
        <a href="1.py">Start Over</a>
    </body>
    
</html>
""")