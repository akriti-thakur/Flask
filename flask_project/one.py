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

# from flask import url_for
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

# if __name__ == '__main__':
#     app.run()


# -----------------------------------------------------------------

# from flask import Flask, request, render_template_string

# app = Flask(__name__)

# @app.route('/')
# def hello():
#    return "hello"
# @app.route('/login', methods=['POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# def do_the_login():
#     # Retrieve the form data
#     username = request.form['username']
#     password = request.form['password']
    
#     # For demonstration purposes, we'll just display the input data.
#     return f'Logging in...<br>Username: {username}<br>Password: {password}'

# def show_the_login_form():
#     # This is where you would render the login form.
#     login_form_html = '''
#     <form method="post" action="/login">
#         <p><input type="text" name="username" placeholder="Username"></p>
#         <p><input type="password" name="password" placeholder="Password"></p>
#         <p><input type="submit" value="Login"></p>
#     </form>
#     '''
#     return render_template_string(login_form_html)

# if __name__ == '__main__':
#     app.run(debug=True)

# -----------------------------------------------------------------------------------------------------
# cookies

# from flask import Flask, request, make_response

# app = Flask(__name__)

# @app.route('/')
# def index():
#     # Check if the cookie is set and display its value
#     username = request.cookies.get('username')
#     if username:
#         return f'Hello, {username}!'
#     else:
#         return 'Hello, stranger!'

# @app.route('/set_cookie/<username>')
# def set_cookie(username):
#     # Create a response object
#     resp = make_response(f'Cookie has been set for {username}')
    
#     # Set a cookie with the username
#     resp.set_cookie('username', username)
    
#     return resp

# @app.route('/delete_cookie')
# def delete_cookie():
#     # Create a response object
#     resp = make_response('Cookie has been deleted')
    
#     # Delete the cookie by setting its expiration to 0
#     resp.set_cookie('username', '', expires=0)
    
#     return resp

# if __name__ == '__main__':
#     app.run(debug=True)



# ------------------------------------------------------------------------------------------------------------
