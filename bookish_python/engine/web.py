from flask import Flask, render_template, request
from webmain import *

app = Flask(__name__)
Books, Members, BookLoans = initialise_databases()


@app.route("/")
def homepage():

    Loan_data = []
    Member_data = Members.getAllData()
    for row in Member_data:
        check_User = str(row['MemberId'])
        Loan_data_line = Books.checkLoans(check_User)
        Loan_data.append(Loan_data_line)

    # remove blanks lists in list of loans
    Loan_data = [ele for ele in Loan_data if ele != []]

    return render_template('homepage.html', Loan_data=Loan_data)

@app.route("/2")
def homepage2():

    # check-in
    BookID = request.args.get('BookID')
    MemberID = request.args.get('MemberID')
    BookLoans.deleteLine(BookID, MemberID)
    Books.editAvailable(1, BookID)

    Loan_data = []
    Member_data = Members.getAllData()
    for row in Member_data:
        check_User = str(row['MemberId'])
        Loan_data_line = Books.checkLoans(check_User)
        Loan_data.append(Loan_data_line)

    # remove blanks lists in list of loans
    Loan_data = [ele for ele in Loan_data if ele != []]

    return render_template('homepage.html', Loan_data=Loan_data)


@app.route("/3")
def homepage3():

    # check-out
    BookID = request.args.get('BookID')
    MemberID = request.args.get('MemberID')

    loan = [{BookLoans.fields[0]: BookID, BookLoans.fields[1]: MemberID}]
    BookLoans.addData(loan)
    Books.editAvailable(-1, BookID)

    Loan_data = []
    Member_data = Members.getAllData()
    for row in Member_data:
        check_User = str(row['MemberId'])
        Loan_data_line = Books.checkLoans(check_User)
        Loan_data.append(Loan_data_line)

    # remove blanks lists in list of loans
    Loan_data = [ele for ele in Loan_data if ele != []]

    return render_template('homepage.html', Loan_data=Loan_data)


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


@app.route("/checkin")
def checkin():

    MemberID = str(request.args.get('MemberID'))
    Loan_data = Books.checkLoans(MemberID)

    return render_template('checkin.html', Loan_data=Loan_data, MemberID=MemberID)


@app.route("/checkout")
def checkout():

    Book_data = Books.getAllData()
    return render_template('checkout.html', Book_data=Book_data)


if __name__ == "__main__":
    app.run()
