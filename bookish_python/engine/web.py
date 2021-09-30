from flask import Flask, render_template, request
from webmain import *

app = Flask(__name__)
Books, Members, BookLoans = initialise_databases()


@app.route("/")
def homepage():

    return render_template('homepage.html')


@app.route("/books")
def books():
    Book_data = Books.getAllData()
    return render_template('books.html', Book_data=Book_data)


@app.route("/books2")
def books2():
    Title = request.args.get('Title')
    Author = request.args.get('Author')
    Total_Copies = request.args.get('Total_Copies')
    Available = request.args.get('Available')
    bookAdded = [{'Title': Title, 'Author': Author, 'TotalCopies': Total_Copies, 'Available': Available}]
    Books.addData(bookAdded)

    Book_data = Books.getAllData()

    return render_template('books.html', Book_data=Book_data)


@app.route("/books3")
def books3():
    Title = request.args.get('Title')
    Author = request.args.get('Author')
    Total_Copies = request.args.get('Total_Copies')
    Available = request.args.get('Available')
    BookID = str(request.args.get('BookID'))
    user_edit = {'Title': Title, 'Author': Author, 'TotalCopies': Total_Copies, 'Available': Available}
    Books.editData(user_edit, BookID)

    Book_data = Books.getAllData()

    return render_template('books.html', Book_data=Book_data)


@app.route("/books4")
def books4():

    BookID = str(request.args.get('BookId'))
    print(BookID)
    print(type(BookID))
    Books.deleteData(BookID)

    Book_data = Books.getAllData()

    return render_template('books.html', Book_data=Book_data)


@app.route("/addBook")
def addBooks():
    return render_template('addbook.html')


@app.route("/editBookId")
def editBookId():
    Book_data = Books.getAllData()
    return render_template('edit_book_Id.html', Book_data=Book_data)


@app.route("/editBookEntry")
def editBookEntry():
    BookId = int(request.args.get('BookId'))
    Book_data = Books.findMatchingID(BookId)
    return render_template('edit_book_entry.html', Book_data=Book_data, BookId=BookId)


@app.route("/deleteBookId")
def deleteBookEntry():
    Book_data = Books.getAllData()
    return render_template('delete_book_Id.html', Book_data=Book_data)


@app.route("/members")
def members():
    Member_data = Members.getAllData()
    return render_template('members.html', Member_data=Member_data)


if __name__ == "__main__":
    app.run()
