from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def helloworld():
    fruits=["apple","orange","mango"]
    return render_template("index.html",items=fruits)

@app.route('/users')
def userlist():
    users=["anu","ram","bobi"]
    return render_template("user.html",users=users)
if __name__=='__main__' :
    app.run(debug=True)
