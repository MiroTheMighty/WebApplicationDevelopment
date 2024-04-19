#!C:\Users\Miro\AppData\Local\Microsoft\WindowsApps\python.exe
import cgi

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
email = form.getvalue('email')
country = form.getvalue('country')

print(f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Korak 2</title>
    </head>
    <body>
        <h1>Korak 2</h1>
        <form action="3.py" method="post">
            First Name: <input type="text" name="first_name" value="{first_name}" required><br><br>
            Last Name: <input type="text" name="last_name" value="{last_name}" required><br><br>
            <input type="hidden" name="email" value="{email}">
            <input type="hidden" name="country" value="{country}">
            <input type="submit" value="Next">
        </form>
    </body>
</html>
""")