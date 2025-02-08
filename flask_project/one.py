# routing
 
# from flask import Flask

# app=Flask(__name__)
# @app.route('/')
# def hello():
#    return 'hello world mode'

# @app.route('/products')
# def product():
#    return 'this is product page'
# if __name__=="__main__":
#     app.run(debug=True,port=9000)
    
#  -------------------------------------------------------------------

# from flask import Flask,render_template

# app=Flask(__name__)
# @app.route('/')
# def hello():
#    return render_template('index.html')
#    # return 'hello world mode'

# @app.route('/products')
# def product():
#    return 'this is product page'
# if __name__=="__main__":
#     app.run(debug=True )

# -----------------------------------------------------------------

# from markupsafe import escape
# from flask import Flask

# app = Flask(__name__)

# @app.route('/user/<username>')
# def show_user_profile(username):
    
#     # show the user profile for that user
#     return f'User {escape(username)}'



# if __name__=="__main__":
#     app.run(debug=True )

# ----------------------------------------------------------------
# URL Building

from flask import url_for
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.run()
