from flask import Flask, render_template, request
import base64, logging

logging.basicConfig(filename='web_service.log', level=logging.DEBUG)
 

app = Flask(__name__)
 

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api')
def readfile():
    try:
        with open(request.args.get('filename'), 'r') as file:
            return render_template("image_indiv.html", file_content=file.read())
        
    except:
        with open(request.args.get('filename'), 'rb') as file:
            return render_template("image_indiv.html", file_content=base64.b64encode(file.read()).decode()) #return image file as base64
 

if __name__ == '__main__':
 
    app.run(host="0.0.0.0",debug=True)
