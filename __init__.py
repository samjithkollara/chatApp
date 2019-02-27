from flask import Flask,render_template


app = Flask(__name__)
app.config['SECRET_KEY']='mysecretket'


@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')


if __name__ == '__main__':
    app.run(port=5656,debug=True)


