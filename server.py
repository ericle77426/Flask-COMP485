import sqlite3, smtplib, os, subprocess
from flask import Flask, request, session, g, render_template, flash, \
									redirect, url_for
from contextlib import closing
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
app.config.from_pyfile('config.cfg') # Initialize app's settings from config.cfg

# Helper function to connect to SQLite3
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

# Helper function to init SQLite3 db when app starts
def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

# Initialize DB connection for each request and tear them down afterwards
@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()


# Ping a specific host and report its status
def isAlive(server):
	command = ['ping', '-n', '1', '-w', '1000', server]
	with open(os.devnull, 'w') as DEVNULL:
		res = subprocess.call(command, stdout=DEVNULL, stderr=DEVNULL)

############## APP ROUTES ################

# This route is for homepage, always displays all monitored servers
@app.route('/')
def index():
	cur = g.db.execute("select * from servers order by name")
	serverList = [dict(id=row[0], serverName=row[1], status=isAlive(row[1])) for row in cur.fetchall()]
	

	return render_template("index.html", serverList=serverList)

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
	# If method = POST, validate username & password then decide
	error = None
	if request.method == 'POST':
		cur = g.db.execute("select * from users")
		# Get all users and convert the result to a dictionary, otherwise a tuple
		userList = [dict(username=row[0], password=row[1]) for row in cur.fetchall()]
		inputUser = request.form['username']
		inputPass = request.form['password']

		usernameList = [u.get('username') for u in userList]

		if inputUser not in usernameList:
			error = "Username does not exist"
		else:
			for user in userList:
				if user['username'] == inputUser:
					if user['password'] != inputPass:
						error = "Incorrect password"
					else:
						session['logged_in'] = True
						flash('You are logged in')
						return redirect(url_for('index'))

	# If method = GET, simply displays login page
	return render_template('login.html', error=error)


if __name__ == "__main__":
	app.run()