#!C:\Users\Miro\AppData\Local\Microsoft\WindowsApps\python.exe
from subjects import subjects
from http import cookies
import cgi, os, re


cookie = cookies.SimpleCookie()
form = cgi.FieldStorage()

if form.getvalue('year') is not None:
    year = int(form.getvalue('year'))
else:
    year = 1


def save_cookie(subject):
    sanitized_subject = re.sub(r'\s+', '_', subject)
    radio_value = form.getvalue(subject)
    cookie[sanitized_subject] = radio_value
    print(cookie.output())

def save_all_subject_cookies():
    for subject_key, subject_value in subjects.items():
        if subject_value['year'] == year - 1:
            save_cookie(subject_value['name'])
    print('Content-Type: text/html\n')

def load_cookie():
    if os.environ.get('HTTP_COOKIE', ''):
        existing_cookies = os.environ.get('HTTP_COOKIE', '').split('; ')
        for cookie_str in existing_cookies:
            cookie.load(cookie_str)

def print_upisni_list():
    print("""
        <tr>
            <th>Subject</th>
            <th>Status</th>
        </tr>
    """)
    for cookie_name, cookie_value in cookie.items():
        subject_name = cookie_name.replace('_', ' ')
        status_value = cookie_value.value.replace('_', ' ')
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
            cookie_value = ''
            if str(subject_value['name']).replace(' ', '_') in cookie:
                cookie_value = cookie[str(subject_value['name']).replace(' ', '_')].value
            print_selection_radio(subject_value['name'], cookie_value)

save_all_subject_cookies()
load_cookie()
print(f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cookies</title>
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