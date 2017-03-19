from flask import Flask, render_template, request
from main import txtspeech
app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def urlinput():
    url = request.form['urlenter']
    print ("URL Parsed: %s" % url)
    txtspeech(url)
    return 'ok'



if __name__ == "__main__":
    app.run()