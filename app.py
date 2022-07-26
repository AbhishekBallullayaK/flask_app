from flask import Flask,render_template,request
import pickle
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

database = {'Abhishek':'abhi18@123','Anujna':'anu05@123','Ashik':'ashik@123'}

@app.route('/form_login',methods = ['POST','GET'])
def login():
    user = request.form['username']
    pwd = request.form['password']

    if user not in database:
        return render_template('login.html',info='invalid username')
    elif database[user]!=pwd:
        return render_template('login.html', info='invalid password')
    else:
        return render_template('profile.html',name=user)

if __name__ == '__main__':
    app.run(debug=True)







