from flask import Flask, render_template, request
 

app = Flask(__name__)
 

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api')
def readfile():
    with open(request.args.get('filename')) as file:
        data = file.readlines()
    
    return f"<p>{data}</p>"
 

if __name__ == '__main__':
 
    app.run(host="0.0.0.0",debug=True)
