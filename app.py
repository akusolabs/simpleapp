
from time import strftime
from flask import Flask, render_template, request, flash, json
from forms import ContactForm
from flaskext.mysql import MySQL
# from werkzeug import generate_password_hash, check_password_hash



app = Flask(__name__)

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


