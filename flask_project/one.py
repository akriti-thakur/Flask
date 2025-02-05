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

from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def hello():
   return render_template('index.html')
   # return 'hello world mode'

@app.route('/products')
def product():
   return 'this is product page'
if __name__=="__main__":
    app.run(debug=True )

