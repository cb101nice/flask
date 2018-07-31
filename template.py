from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    name = "Jose"
    letters = list(name)
    pup_dictionary = {'pup_name':'Sammy'}
    return render_template('basic.html', sentvalue=name, 
    letters=letters, pup_dictionary=pup_dictionary)
@app.route('/dialogue')
def dia():
    return render_template('dialogue.html')
if __name__ == '__main__':
    app.run(debug=True)