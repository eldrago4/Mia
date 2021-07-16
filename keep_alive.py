from flask import Flask, url_for ,session
from flask import render_template, redirect
from authlib.integrations.flask_client import OAuth
import threading
import google
import threading 
from google_auth_oauthlib import flow

# Flask Config Stuff
app = Flask(__name__)
app.secret_key = '!secret'
app.config.from_object('config')

# Google Oath + Scope
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth = OAuth(app)
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'https://www.googleapis.com/auth/spreadsheets'
        # Scope as defined in google developer consol
    }
)


# Threading initialization might go here
# One thread for the listening discord bot
content1 = {'content': 'Hello from bot1'}
#t3 = threading.Thread(target=starbot.run())
#t3.start()

# Flask Routes
@app.route('/')
def home():
    # Start Flask user 'Session'
    user = session.get('user')
    return render_template('index.html', user=user)


@app.route('/authorize')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route('/auth')
def auth():
    # Get Token and User data
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)

    # start flask user 'session'
    session['user'] = user

    # return to homepage / root directory
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')
    
def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()