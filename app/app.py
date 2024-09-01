from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL
from flask import request, redirect, url_for

app = Flask(__name__)

#MYSQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_db'] = 'biblos12'            
mysql = MySQL(app)

#settings
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return render_template('Books/index.html')


@app.route('/Books/books')
def books():
    try:
        cur = mysql.connection.cursor()
        cur.execute('USE biblos12')  # Select the database
        cur.execute('SELECT * FROM titles')
        data = cur.fetchall()
        #print(data)  # For debugging purposes
        return render_template('Books/books.html')
    except Exception as e:
        # Handle the exception (e.g., log it or return an error page)
        return f"Error: {str(e)}"

    
@app.route("/Books/addbooks", methods=['GET','POST'])
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
        



@app.route('/edit')
def edit_book():
    return render_template('Books/edit_book.html')


@app.route('/delete/<string:id>')
def delete_book(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('USE biblos12')  # Select the database
        cur.execute('DELETE * FROM titles WHERE id {0}'.format(id))
        print(data)  # For debugging purposes
        return redirect(url_for('Books/books.html'))
    except Exception as e:
    # Handle the exception (e.g., log it or return an error page)
        return f"Error: {str(e)}"
        return 'delete book'












    


    
    
    
    
    
    
    
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)




    