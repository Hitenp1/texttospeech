from flask import Flask, render_template,request,redirect,url_for
from main import txtspeech
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/outcome')
def urlinput():
    #url = request.form['urlenter']
    url = request.args.get('urlenter')
    print ("URL Parsed: %s" % url)
    display = txtspeech(url)
    # print (display)
    return render_template('index.html', display=display)
    #return redirect(url_for('results'))

# @app.route('/result')
# def results():
#     display = 'COOKIES'
#     return render_template('result.html', display=display)


if __name__ == "__main__":
    app.run(port=3000, debug=True)


#auto reloading variables

# from jinja2 import Environment, PackageLoader, select_autoescape
# env = Environment(
#     loader=PackageLoader('yourapplication', 'templates'),
#     autoescape=select_autoescape(['html'])
# )

