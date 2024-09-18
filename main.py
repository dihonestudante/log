from flask import Flask, render_template,redirect, request,flash

app = Flask(__name__)
app.config['SECRET_KEY']= "DIHONE"
@app.route("/")
def home():
  return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
  nome = request.form.get('nome')
  senha =  request.form.get('senha')
  
  if nome == 'dihone' and senha=='123':
    return render_template('usuario.html')
  else:
    flash('USUARIO INVALIDO')
    return redirect('/')

if __name__ == "__main__":
  app.run(debug=True)