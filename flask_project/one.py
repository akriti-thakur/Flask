# routing
 
from flask import Flask

app=Flask(__name__)
@app.route('/')
def hello():
   return 'hello world mode'

@app.route('/products')
def product():
   return 'this is product page'
if __name__=="__main__":
    app.run(debug=True )
    
#  -------------------------------------------------------------------

   

