from flask import Flask, render_template, url_for, request,redirect
import csv
app = Flask(__name__)


def database(data):
    with open('database.txt', 'a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        db.write(f'\n{email},{subject},{message}')

def database_CSV(data):
    with open('database.csv', newline="",mode='a') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email, subject, message])


@app.route('/<string:page_name>')
def my_home(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods= ['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        database_CSV(data)
        return redirect('thankyou.html')
    else:
        return 'Something went wrong. Try again!'

