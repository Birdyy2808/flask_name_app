from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    names=[{
        "name":"Vaibhav"
    },
    {
        "name":"Geeta"
    },
    {
        "name":"Balwant"
    }
    ]

    return render_template('index.html', users=names)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
