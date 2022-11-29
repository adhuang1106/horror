from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] != 'tao666tao':
            error = 'Invalid Credentials. Please try again.'
        elif request.form['password'] == 'tao666tao':
            return render_template('desktop.html')
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/folder', methods=['GET','POST'])
def folder():
    if request.method == 'GET':
        return render_template('folder.html')
    return render_template('folder.html')

if __name__ == "__main__":
    app.debug = True
    app.run()