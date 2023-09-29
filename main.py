from flask import Flask, request, make_response,redirect,render_template,session,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
import unittest
app = Flask(__name__)
app.debug=True
bootstrap= Bootstrap(app)
app.config['SECRET_KEY'] = "SUPER SECRETO"
lista = ["1","2","3","5","6","7","8"]

class LoginForm(FlaskForm):
    username=StringField('Nombre de Usuario',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit= SubmitField("Enviar")

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
    pass
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html",error=error)
@app.route('/')
def index():
    user_ip =request.remote_addr
    response = make_response(redirect("/hello"))
    session['user_ip']=user_ip
    return response

@app.route('/hello',methods=['GET','POST'])
def hello():
    user_ip =session.get("user_ip")
    login_form =LoginForm()
    username = session.get('username')
    context={'user_ip': user_ip,
             'lista': lista,
             'login_form':login_form,
             'username':username}

    if login_form.validate_on_submit():
        username= login_form.username.data
        session['username']=username
        flash('Nombre de usuario registrado con éxito')
        return redirect(url_for('index'))
    return render_template("hello",**context)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
