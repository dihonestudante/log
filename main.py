from flask import Flask
from flask import render_template

#Instancia
app = Flask(__name__)

#Rota Principal
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)