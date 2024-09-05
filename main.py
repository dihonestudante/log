from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/cliente')
def cliente():
    return render_template('cliente.html')

@app.route('/cliente/<cliente_id>')
def cliente_id(cliente_id):
    return render_template('cliente_id.html',cliente_id=cliente_id)

if __name__ == "__main__":
    app.run(debug=True)