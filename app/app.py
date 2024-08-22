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

    
@app.route("/books/addbooks", methods=['GET','POST'])
def addbooks():
    if request.method == 'POST':
        title = request.form['title']
        location = request.form['location']
        isbn = request.form['isbn']
        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO titles (title, location, isbn) VALUES (%s, %s, %s)', (title, location, isbn))
        mysql.connection.commit()
        return render_template('index.html')
        

#@app.route('/edit')
def edit_book():
    return render_template('Books/edit_book.html')


@app.route('/delete')
def delete_book():
    return 'delete book'


@app.route('/books/addbooks/save')
def addbooks_save():
    title = request.form['title']
    location = request.form['location']
    isbn = request.form['isbn']
    author = request.form['idauthor']
    editorial = request.form['ideditorial']
    
    sql="INSERT INTO titles(title, location, isbn, idauthor, ideditorial) VALUES(%s, %s, %s)" 
    data=(title, location, isbn, idauthor, ideditorial)
    


    
    
    
    
    
    
    
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)




    