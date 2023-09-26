from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)
# app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

@app.get('/')
def root_get():
    if request.cookies.get('user_name'):
        return render_template ('layout.html', username=request.cookies.get('user_name'))
    return redirect(url_for('register_get'))

@app.post('/')
def root_post():
    response = make_response(redirect(url_for('register_get')))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response

@app.get('/register/')
def register_get():
    return render_template('inputform.html')

@app.post('/register/')
def register_post():
    # устанавливаем cookie
    response = make_response(redirect(url_for('root_get')))
    response.set_cookie('user_name', request.form['username'])
    response.set_cookie('user_email', request.form['electromail'])
    return response


if __name__ == '__main__':
    app.run(debug=True)