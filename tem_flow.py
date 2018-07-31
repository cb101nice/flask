from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    puppies = ['Fluffy', 'Rufus', 'Spike']
    mylist = [1,2,3,4,5]
    return render_template('jinja.html',mylist=mylist,puppies=puppies)
if __name__ == '__main__':
    app.run(debug=True)