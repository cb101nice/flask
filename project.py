from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('house.html')

@app.route('/house')
def house():
    return render_template('house.html')

@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html')

@app.route('/conv')
def conv():
    return render_template('conv.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# @app.route('/name_check_ent')
# def name_check_ent():
#     return render_template('name_check_ent.html')

# @app.route('/name_check_che')
# def name_check_che():
#     username = request.args.get('username')
#     return render_template('name_check_che.html',username=username)

if __name__ == '__main__':
    app.run(debug=True)