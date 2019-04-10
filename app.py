# flask_web/app.py

from flask import Flask
# app = Flask(__name__)
app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/')
def hello_world():
   return 'Hey, we have Flask in a Docker container! Static'

if __name__ == "__main__":   
  app.run(debug=True, host='0.0.0.0')