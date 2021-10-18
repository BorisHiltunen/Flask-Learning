from flask import Flask, render_template, request
from flask_script import Manager, Command, Shell

app = Flask(__name__)
app.debug  = True
manager = Manager(app)

class Faker(Command):
    'A command to add fkae data to the tables'
    def run(self):
        # add Logic here
        print("Fake data entered")

def shell_context():
    import os, sys
    return dict(app=app, os=os, sys=sys)

manager.add_command("shell", Shell(make_context=shell_context))

manager.add_command("faker", Faker())

@manager.command
def foo():
    "Just a simple command"
    print("foo command executed")

@app.route('/')
def index():
    return render_template('index.html', name='Jerry')

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    return "All Books in {} category".format(genre)

@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside 
        password = request.form.get('password')

        if username == 'root' and password == 'pass':
            message = "Correct username and password"
        else:
            message = "Wrong username or password"

    return render_template('login.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)