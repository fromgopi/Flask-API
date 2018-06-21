"""from flask import Flask, render_template, Blueprint

app = Flask(__name__)
app.config['TESTING'] = True


@app.route('/')
def index():
    try:
        app.logger.debug('Simple Debbuging smts')
        return render_template('api/templates/index.html')
    except:
        print("N/A")


@app.route('/name')
def getName():
    user = {'username': 'Gopi Krishna'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('name.html', user=user, posts=posts)"""


from api import app

if __name__ == '__main__':
    app.run()
