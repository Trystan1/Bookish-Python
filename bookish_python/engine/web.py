from flask import Flask, render_template, request
from webmain import *

app = Flask(__name__)


@app.route("/")
def index():
    present_options()
    return render_template('index.html')


@app.route("/busInfo")
def busInfo():

    console_command = request.args.get('console_command')
    Books, Members, BookLoans = initialise_databases()
    Book_data = run_UI(Books, Members, BookLoans, console_command)
    statement = displayDataNew(Book_data, Books)
    print(statement)

    return render_template('info.html', console_command=console_command, statement=statement)


if __name__ == "__main__":
    app.run()
