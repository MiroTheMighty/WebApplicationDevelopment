#!C:\Users\Miro\AppData\Local\Microsoft\WindowsApps\python.exe
import cgi

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
email = form.getvalue('email')
country = form.getvalue('country')

print(f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Korak 1</title>
    </head>
    <body>
        <h1>Korak 1</h1>
        <form action="2.py" method="post">
            Email: <input type="email" name="email" value="{email}" required><br><br>
            Country:
            <select name="country">
                <option value="Croatia" {"selected" if country=="croatia" else ""}>Croatia</option>
                <option value="France" {"selected" if country=="france" else ""}>France</option>
                <option value="Italy" {"selected" if country=="italy" else ""}>Italy</option>
                <option value="Germany" {"selected" if country=="germany" else ""}>Germany</option>
            </select><br><br>
            <input type="submit" value="Next">
        </form>
    </body>
</html>
""")