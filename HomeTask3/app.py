from flask import Flask, request, make_response, render_template, redirect, url_for
from models import db, User


app = Flask(__name__)
# app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.get('/')
def root_get():
    return redirect(url_for('register_get'))

@app.get('/register/')
def register_get():
    return render_template('inputform.html')

@app.post('/register/')
def register_post():
    user = User(request.form['username'],request.form['electromail'],request.form['password'])
    db.session.add(user)
    db.session.commit
    return render_template('layout.html', username=f'{user}')

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")

if __name__ == '__main__':
    app.run(debug=True)