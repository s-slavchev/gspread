from flask import Flask, request, render_template
import gspread

app = Flask(__name__)
app.debug = True

gc = gspread.service_account(filename='active-tome-315415-4618f1423cfb.json')

sheet = gc.open("ReadWrite with Python and gspread").sheet1

def append_name(name):
    names = sheet.get_all_values()
    names.append([name])
    sheet.update('A1', names)

@app.route('/', methods=['GET', 'POST'])
def index():

    name = ''

    if request.method == "POST":
        name = request.form['name']
        append_name(name)


    return render_template('index.html', name=name)



