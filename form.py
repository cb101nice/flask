from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home_form.html')

@app.route('/signup_form')
def signup_form():
    return render_template('sign_up_form.html')

@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thank_you_form.html',first=first,last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/name_check_ent')
def name_check_ent():
    return render_template('name_check_ent.html')

@app.route('/name_check_che')
def name_check_che():
    username = request.args.get('username')
    return render_template('name_check_che.html',username=username)

if __name__ == '__main__':
    app.run(debug=True)