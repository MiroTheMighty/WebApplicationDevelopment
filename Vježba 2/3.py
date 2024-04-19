#!C:\Users\Miro\AppData\Local\Microsoft\WindowsApps\python.exe
import cgi

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
email = form.getvalue('email')
country = form.getvalue('country')
username = form.getvalue('username')
password = form.getvalue('password')

print(f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Korak 3</title>
    </head>
    <body>
        <h1>Korak 3</h1>
        <form action="kraj.py" method="post">
            Username: <input type="text" name="username" required><br><br>
            Password: <input type="password" name="password" required><br><br>
            <input type="hidden" name="email" value="{email}">
            <input type="hidden" name="country" value="{country}">
            <input type="hidden" name="first_name" value="{first_name}">
            <input type="hidden" name="last_name" value="{last_name}">
            <input type="submit" value="Finish">
        </form>
    </body>
</html>
""")
