from flask import Flask, render_template, request, redirect, url_for
from science import runscience
from files import runfiles
from IT import runIT
from forums import runforums
from videos import runvideos

app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['searchbar']
        query = query.strip()
        if query == "":
            return render_template("index.html")
        tab = request.form['tabs']
        if tab.lower().strip() == 'science':
            return redirect(url_for('science', query=query))
        if tab.lower().strip() == 'it':
            return redirect(url_for('it', query=query))
        if tab.lower().strip() == 'files':
            return redirect(url_for('files', query=query))
        if tab.lower().strip() == 'videos':
            return redirect(url_for('videos', query=query))
        if tab.lower().strip() == 'forums':
            return redirect(url_for('forums', query=query))
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/search?q=<query>&cat=science', methods=['GET', 'POST'])
def science(query):
    if request.method == 'POST':
        query = request.form['searchbar']
        query = query.strip()
        if query == "":
            return render_template("index.html")
        tab = request.form['tabs']
        if tab.lower().strip() == 'science':
            return redirect(url_for('science', query=query))
        if tab.lower().strip() == 'it':
            return redirect(url_for('it', query=query))
        if tab.lower().strip() == 'files':
            return redirect(url_for('files', query=query))
        if tab.lower().strip() == 'videos':
            return redirect(url_for('videos', query=query))
        if tab.lower().strip() == 'forums':
            return redirect(url_for('forums', query=query))
    answer = runscience(query)
    print(answer)
    return render_template('science.html', query_value=query, answers=answer)

@app.route('/search?q=<query>&cat=videos', methods=['GET', 'POST'])
def videos(query):
    if request.method == 'POST':
        query = request.form['searchbar']
        query = query.strip()
        if query == "":
            return render_template("index.html")
        tab = request.form['tabs']
        if tab.lower().strip() == 'science':
            return redirect(url_for('science', query=query))
        if tab.lower().strip() == 'it':
            return redirect(url_for('it', query=query))
        if tab.lower().strip() == 'files':
            return redirect(url_for('files', query=query))
        if tab.lower().strip() == 'videos':
            return redirect(url_for('videos', query=query))
        if tab.lower().strip() == 'forums':
            return redirect(url_for('forums', query=query))
    answer = runvideos(query)
    return render_template('videos.html', query_value=query, answers=answer)

@app.route('/search?q=<query>&cat=it', methods=['GET', 'POST'])
def it(query):
    if request.method == 'POST':
        query = request.form['searchbar']
        query = query.strip()
        if query == "":
            return render_template("index.html")
        tab = request.form['tabs']
        if tab.lower().strip() == 'science':
            return redirect(url_for('science', query=query))
        if tab.lower().strip() == 'it':
            return redirect(url_for('it', query=query))
        if tab.lower().strip() == 'files':
            return redirect(url_for('files', query=query))
        if tab.lower().strip() == 'videos':
            return redirect(url_for('videos', query=query))
        if tab.lower().strip() == 'forums':
            return redirect(url_for('forums', query=query))
    answer = runIT(query)
    return render_template('IT.html', query_value=query, answers=answer)

@app.route('/search?q=<query>&cat=files', methods=['GET', 'POST'])
def files(query):
    if request.method == 'POST':
        query = request.form['searchbar']
        query = query.strip()
        if query == "":
            return render_template("index.html")
        tab = request.form['tabs']
        if tab.lower().strip() == 'science':
            return redirect(url_for('science', query=query))
        if tab.lower().strip() == 'it':
            return redirect(url_for('it', query=query))
        if tab.lower().strip() == 'files':
            return redirect(url_for('files', query=query))
        if tab.lower().strip() == 'videos':
            return redirect(url_for('videos', query=query))
        if tab.lower().strip() == 'forums':
            return redirect(url_for('forums', query=query))
    answer = runfiles(query)
    return render_template('files.html', query_value=query, answers=answer)

@app.route('/search?q=<query>&cat=forums', methods=['GET', 'POST'])
def forums(query):
    if request.method == 'POST':
        query = request.form['searchbar']
        query = query.strip()
        if query == "":
            return render_template("index.html")
        tab = request.form['tabs']
        if tab.lower().strip() == 'science':
            return redirect(url_for('science', query=query))
        if tab.lower().strip() == 'it':
            return redirect(url_for('it', query=query))
        if tab.lower().strip() == 'files':
            return redirect(url_for('files', query=query))
        if tab.lower().strip() == 'videos':
            return redirect(url_for('videos', query=query))
        if tab.lower().strip() == 'forums':
            return redirect(url_for('forums', query=query))
    answer = runforums(query)
    return render_template('forums.html', query_value=query, answers=answer)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
