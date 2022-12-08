from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] != 'tao666tao':
            if request.form['password'] == 'grplqhphxvoxflihu':
                return redirect(url_for('blog') ,code=307)
            error = 'Invalid Credentials. Please try again.'
        elif request.form['password'] == 'tao666tao':
            return render_template('desktop.html')
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/folder', methods=['GET','POST'])
def folder():
    if request.method == 'POST':
        return render_template('folder.html')
    return redirect(url_for('login'))

@app.route('/blog', methods=['GET','POST'])
def blog():
    if request.method =='POST':
        return render_template('blog.html')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.run()