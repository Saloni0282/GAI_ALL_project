from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data as a Python dictionary (our "database")
data = {}

@app.route('/')
def welcome():
    return render_template('home.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        
        # Check if the key already exists
        if key in data:
            return "Key already exists. Use the update route to modify the value."
        
        data[key] = value
        return redirect(url_for('read'))
    
    return render_template('create.html')

@app.route('/read')
def read():
    return render_template('read.html', data=data)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            data[key] = request.form['value']
            return redirect(url_for('read'))
    
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            del data[key]
            return redirect(url_for('read'))
    
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)
