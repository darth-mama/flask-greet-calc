from flask import Flask

app = Flask(__name__)


@app.route('/welcome/back')
def welcome_back():
    html = """
    <html>
      <body>
        <h1>Welcome back</h1>
      </body>
    </html>
    """
    return html


@app.route('/welcome/home')
def welcome_home():
    html = """
    <html>
      <body>
        <h1>Welcome home</h1>
      </body>
    </html>
    """
    return html


@app.route('/welcome')
def welcome():
    html = """
    <html>
      <body>
        <h1>Welcome</h1>
      </body>
    </html>
    """
    return html
