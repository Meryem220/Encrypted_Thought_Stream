from flask import Flask, render_template, request, redirect, url_for
from cryptography.fernet import Fernet
import sqlite3
app = Flask(__name__)

# Connect to SQLite database. It will be created if it doesn't exist.
connection = sqlite3.connect("thoughts.db")
# In order to execute SQL statements and fetch results from the database, we need a cursor object.
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS thoughts (id INTEGER PRIMARY KEY AUTOINCREMENT, thought TEXT, encrypted TEXT)")
# Now that we have a connection and a cursor we can create a database table 
@app.route('/')
def index():
  return render_template('index.html', database = None)

@app.route('/add')
def add():
  return render_template('add.html')

@app.route('/login')
def login():
  pass

@app.route('/logout')
def login():
  pass

@app.route('/remove')
def add():
  return render_template('add.html')

@app.route('/update')
def add():
  return render_template('add.html')