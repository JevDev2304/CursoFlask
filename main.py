from flask import Flask, request, make_response,redirect,render_template

app = Flask(__name__)
lista = ["1","2","3","5","6","7","8"]
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html",error=error)
@app.route('/')
def index():
    user_ip =request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip", user_ip)
    return response

@app.route('/hello')
def hello_world():
    user_ip =request.cookies.get("user_ip")
    context={'user_ip': user_ip,
             'lista': lista}
    return render_template("hello.html",**context)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
