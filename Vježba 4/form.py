#!C:/Users/Miro/AppData/Local/Microsoft/WindowsApps/python.exe
from subjects import subjects
import session
import db
import cgi
import os

form = cgi.FieldStorage()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(form)

session_id = session.get_or_create_session_id()
_, data = db.get_session(session_id)

if form.getvalue('year') is not None:
    year = int(form.getvalue('year'))
else:
    year = 1

def print_subject(year):
    if year != 4:
        print(f"""
                <tr>
                    <th>Year {year}</th>
                    <th>Status</th>
                </tr>
        """)
    for subject_key, subject_value in subjects.items():
        if subject_value['year'] == year:
            print(f"""
                <tr>
                    <td>{subject_value['name']}</td>
            """)
            data_value = ''
            subject_name = str(subject_value['name']).replace(' ', '_')
            if subject_name in data:
                data_value = data[subject_name]
            print_selection_radio(subject_name, data_value)

def print_upisni_list():
    print("""
        <tr>
            <th>Subject</th>
            <th>Status</th>
        </tr>
    """)
    
    for subject_name, status_value in data.items():
        subject_name = subject_name.replace('_', ' ')
        status_value = status_value.replace('_', ' ')
        print(f"""
            <tr>
                <td>{subject_name}</td>
                <td>{status_value}</td>
            </tr>
        """)

def print_selection_radio(subject, cookie_value):
    print(f"""
                    <td>
                        <input type="radio" id="ne_upisuje_{subject}" name="{subject}" value="ne_upisuje" {'checked' if cookie_value == 'ne_upisuje' else ''}>
                        <label for="ne_upisuje">Ne upisuje</label>
                        <input type="radio" id="upisuje_{subject}" name="{subject}" value="upisuje" {'checked' if cookie_value == 'upisuje' else ''}>
                        <label for="upisuje">Upisuje</label>
                        <input type="radio" id="polozen_{subject}" name="{subject}" value="polozen" {'checked' if cookie_value == 'polozen' else ''}>
                        <label for="polozen">Polozen</label>
                    </td>
                </tr>
    """)

print(f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Session</title>
    </head>
    <body>
        <form method="post">
            <button type="submit" name="year" value="1">1st year</button>
            <button type="submit" name="year" value="2">2nd year</button>
            <button type="submit" name="year" value="3">3rd year</button>
            <button type="submit" name="year" value="4">Upisni list</button>
        
            <table border="1">
""")

if year == 4:
    print_upisni_list()
else:
    print_subject(year)

print(f"""
            </table>
        </form>
    </body>
</html>
""")