from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MYSQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'biblos12'
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    return render_template('Books/index.html')


@app.route('/Books/books', methods=['GET', 'POST'])
def books():
    try:
        cur = mysql.connection.cursor()
        #cur.execute('USE biblos12')  # Select the database
        cur.execute('SELECT * FROM titles')
        data = cur.fetchall()
        print(data)  # For debugging purposes
        return render_template('Books/books.html', titles=data)
    except Exception as e:
        # Handle the exception (e.g., log it or return an error page)
        return f"Error: {str(e)}"


@app.route("/Books/addbooks", methods=['GET', 'POST'])
def addbooks():
    if request.method == 'POST':
        title = request.form['title']
        location = request.form['location']
        isbn = request.form['isbn']
        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO titles (title, location, isbn) VALUES (%s, %s, %s)', (title, location, isbn))
        mysql.connection.commit()
        return redirect(url_for('index'))


@app.route('/Books/edit_book/<id>')
def edit_book( id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT title, location , isbn FROM titles WHERE id = %s", (id,))
        title = cur.fetchone()
        mysql.connection.commit()    
        return render_template('Books/edit_book.html', title=title)
    except Exception as e:
        # Handle the exception (e.g., log it or return an error page)
        return f"Error: {str(e)}"

@app.route('/update/<id>')
def update_title(id):
    if request.method == 'POST':
        title = request.form['title']
        location = request.form['location']
        isbn = request.form['isbn']
        cur = mysql.connection.cursor()
        data = cur.fetchall()
        cur.execute("""
        UPDATE titles
        SET title = %s
            location = %s
            isbn = %s
        WHERE id = %s    
        """,(title, location, isbn, id))
        mysql.connection.commit()
        print(data)  # For debugging purposes
        return render_template('Books/books.html', titles=data)
        

@app.route("/delete_book/<id>", methods=['GET', 'POST'])
def delete_book(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('USE biblos12')  # Select the database
        cur.execute('DELETE FROM titles WHERE id=%s',(id,))
        mysql.connection.commit()

        # Fetch updated data (if needed)
        cur.execute('SELECT * FROM titles')
        data = cur.fetchall()
        print(data)  # For debugging purposes

        return render_template('Books/books.html', titles=data)
    except Exception as e:
        # Handle the exception (e.g., log it or return an error page)
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(port=5000, debug=True)

































































