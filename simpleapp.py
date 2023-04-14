
from time import strftime
from flask import Flask, render_template, request, flash, json
from forms import ContactForm
from flaskext.mysql import MySQL
# from werkzeug import generate_password_hash, check_password_hash
from elasticapm.contrib.flask import ElasticAPM



app = Flask(__name__)
app.debug = True
app.config['ELASTIC_APM'] = {
  'SERVICE_NAME': 'simple-app',
  'SECRET_TOKEN': '2WK2yZvHssER0ZrXJ2',
  'SERVER_URL': 'https://a12c50be85804ff298e2bb5ce1770777.apm.us-central1.gcp.cloud.es.io:443',
  'ENVIRONMENT': 'dev-gke',
}

apm = ElasticAPM(app)


#app.config.from_pyfile('config.py')

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def home():
  # newrelic.agent.set_transaction_name("Home")
  return render_template('home.html')

@app.route('/about')
def about():
  # newrelic.agent.set_transaction_name("About")
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  # # newrelic.agent.set_transaction_name("Contact")
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
    # newrelic.agent.set_transaction_name("ShowSignUp")
    return render_template('signup.html')
 
@app.route('/signUp',methods=['POST'])
def signUp():
    # newrelic.agent.set_transaction_name("SignUp")
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    # validate the received values
    if _name and _email and _password:
      conn = mysql.connect()
      cursor = conn.cursor()
      #_hashed_password = generate_password_hash(_password)
      cursor.callproc('sp_createUser',(_name,_email,_password))
      data = cursor.fetchall()
      if len(data) == 0:
        conn.commit()
        return json.dumps({'message':'User created successfully !'})
      else:
        return json.dumps({'error':str(data[0])})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
    
    conn = mysql.connect()
    cursor = conn.cursor()
    _hashed_password = generate_password_hash(_password)
    cursor.callproc('./sp_createUser.sql',(_name,_email,_hashed_password))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8899)
