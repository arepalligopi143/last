from flask import Flask
app = Flask(__name__)
@app.route('/index')
def index():
 return 'Index Page goes here'
@app.route("/")
def main():
 return "This is your main page!"
if __name__ == '__main__':
 app.run()