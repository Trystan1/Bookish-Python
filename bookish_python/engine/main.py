from database_creator import DataBase


def initialise_databases():
        Books = DataBase('Books', ['BookId', 'Title', 'Author', 'TotalCopies', 'Available'],
                         ['INTEGER PRIMARY KEY AUTOINCREMENT', 'TEXT', 'TEXT', 'INTEGER', 'INTEGER'])
        Books.createTable()

        BookLoans = DataBase('BookLoans', ['BookId', 'MemberId'], ['INTEGER', 'INTEGER'])
        BookLoans.createTable()

        Members = DataBase('Members', ['MemberId', 'FirstName', 'LastName'], ['INTEGER PRIMARY KEY AUTOINCREMENT', 'TEXT',
                                                                              'TEXT'])
        Members.createTable()

        return Books, Members, BookLoans


def input_dummy_data(Books, Members, BookLoans):
        users = [
                {'FirstName': 'Jane', 'LastName': 'Goodall'},
                {'FirstName': 'Rachel', 'LastName': 'Carson'},
                {'FirstName': 'Barry', 'LastName': 'Bishop'},
                {'FirstName': 'Trystan', 'LastName': 'Jones'},
                {'FirstName': 'Agent', 'LastName': 'Smith'},
                {'FirstName': 'Jane', 'LastName': 'Doe'}
                ]

        Members.addData(users)

        books = [
                {'Title': 'The Lord of the Rings', 'Author': 'J.R.R Tolkien', 'TotalCopies': 1, 'Available': 0},
                {'Title': 'Harry Potter', 'Author': 'J.K Rowling', 'TotalCopies': 1, 'Available': 0},
                {'Title': 'The Colour of Magic', 'Author': 'Terry Pratchett', 'TotalCopies': 1, 'Available': 1},
                {'Title': 'The Martian', 'Author': 'Andy Weir', 'TotalCopies': 1, 'Available': 0},
                {'Title': 'The Bible', 'Author': 'God', 'TotalCopies': 1, 'Available': 1},
                {'Title': 'The Hitchhikers Guide to the Galaxy', 'Author': 'Douglas Adams', 'TotalCopies': 1, 'Available': 1},
                {'Title': 'Henry V', 'Author': 'William Shakespeare', 'TotalCopies': 1, 'Available': 1},
                ]

        Books.addData(books)

        loans = [
                {'BookId': '1', 'MemberId': '1'},
                {'BookId': '4', 'MemberId': '1'},
                {'BookId': '2', 'MemberId': '2'}
                ]

        BookLoans.addData(loans)


def delete_all_tables(Books, Members, BookLoans):
        Books.destroyTable()
        Members.destroyTable()
        BookLoans.destroyTable()


def displayData(data, Books):

        # print field headings
        print(f'\n')
        statement = ''
        for i in range(0, len(Books.fields)):
                statement += f'{Books.fields[i]: <40}'
        print(statement)

        for i in range(0, len(data)):
                data_statement = ''
                for ii in range(len(data[i])):
                        if data[i][Books.fields[ii]] is not None:       # Accounting for potentially missing data
                                data_statement += f'{data[i][Books.fields[ii]] : <40}'
                        else:
                                pass
                print(data_statement)


def query_user_4_input(Books):
        print(f'\nYou are now adding a new entry to the {Books.name} Table')
        books = []
        books_dict = {}
        for i in range(1, len(Books.fields)):
                User_Input = input(f'Please make your entry for {Books.fields[i]}: ')
                books_dict[f'{Books.fields[i]}'] = User_Input

        books.append(books_dict)
        return books


def run_UI(Books, Members, BookLoans):
        Run = True
        while Run:
                User_Input = input(f'\nWelcome to the Library'
                                   f'\n1: See Books in the Database'
                                   f'\n2: See Library Members in the Database'
                                   f'\n3: Add a new Book to the Database'
                                   f'\n4: Edit the Details of an Existing Book in the Database'
                                   f'\n5: Remove an Existing Book from the Database'
                                   f'\n6: Add a new Member to the Database'
                                   f'\n7: Edit the Details of an Existing Library Member in the Database'
                                   f'\n8: Remove an Existing Member from the Database'
                                   f'\n9: Check-out a Book'
                                   f'\n10: Check-in a Book'
                                   f'\n11: Check the Current Loans for a Given Member'
                                   f'\nPlease Make Your Entry: ')

                if User_Input == 'Quit':
                        break

                elif User_Input == '1':
                        Book_data = Books.getAllData()
                        displayData(Book_data, Books)

                elif User_Input == '2':
                        Member_data = Members.getAllData()
                        displayData(Member_data, Members)

                elif User_Input == '3':
                        books = query_user_4_input(Books)
                        print(books)
                        Books.addData(books)
                        print('Thanks, book added')

                elif User_Input == '4':
                        edit_entry(Books)

                elif User_Input == '5':
                        delete_entry(Books)

                elif User_Input == '6':
                        members = query_user_4_input(Members)
                        Members.addData(members)
                        print('Thanks, new library member added')

                elif User_Input == '7':
                        edit_entry(Members)

                elif User_Input == '8':
                        delete_entry(Members)

                elif User_Input == '9':
                        book_checkout(Books, Members, BookLoans)

                elif User_Input == '10':
                        book_checkin(Books, Members, BookLoans)

                elif User_Input == '11':
                        check_User = input('Please enter a MemberID to see current Loans: ')
                        data = Books.checkLoans(check_User)
                        displayData(data, Books)


def edit_entry(Books):
        BookID = input(f'Please enter the {Books.fields[0]} of the Book/Member that you are searching for: ')
        Book_data = Books.getAllData()
        IDs = []
        for i in range(0, len(Book_data)):
                IDs.append(Book_data[i][Books.fields[0]])

        if int(BookID) in IDs:
                data = Books.findMatchingID(BookID)
                displayData(data, Books)

                user_edit = {}
                for i in range(1, len(Books.fields)):
                        User_Edit = input(f'\nEnter new {Books.fields[i]}: ')
                        user_edit[f'{Books.fields[i]}'] = User_Edit

                Books.editData(user_edit, BookID)
                print('Book/Member Edited')
        else:
                print('Book/Member could not be found')


def delete_entry(Books):
        BookID = input(f'Please enter the {Books.fields[0]} of the Book/Member that you are searching for: ')
        Book_data = Books.getAllData()
        IDs = []
        for i in range(0, len(Book_data)):
                IDs.append(Book_data[i][Books.fields[0]])

        if int(BookID) in IDs:
                data = Books.findMatchingID(BookID)
                displayData(data, Books)

                User_Input = input(f'Would you like to delete this entry? y/n: ')
                if User_Input == 'y':
                        Books.deleteData(BookID)
                print('Book/Member Deleted')

        else:
                print('Book/Member could not be found')


def book_checkout(Books, Members, BookLoans):
        MemberID = input(f'Please enter your MemberID: ')
        BookID = input(f'Please enter the ID of the Book that you want to loan out: ')
        # need a check here if member id is valid and if book id is available
        loan = [{BookLoans.fields[0]: BookID, BookLoans.fields[1]: MemberID}]
        BookLoans.addData(loan)
        BookName = Books.findMatchingID(BookID)[0][Books.fields[1]]
        MemberForeName = Members.findMatchingID(MemberID)[0][Members.fields[1]]
        MemberSurName = Members.findMatchingID(MemberID)[0][Members.fields[2]]
        # [Books.fields[4]] # all of that is just equivalent to '[Available]' will need database function to change
        # that you fool, something like an editData with only the 'Available section filled?' (NEW edit function which
        # only changes available will do the trick).

        print(f'{BookName} (BookId: {BookID}) has been checked out by'
              f' {MemberForeName} {MemberSurName} (MemberId: {MemberID})')


def book_checkin(Books, Members, BookLoans):
        MemberID = input('Please enter the ID of the user returning the book: ')
        MemberForeName = Members.findMatchingID(MemberID)[0][Members.fields[1]]
        MemberSurName = Members.findMatchingID(MemberID)[0][Members.fields[2]]
        print(f"\nBooks currently checked out by {MemberForeName} {MemberSurName}")
        data = Books.checkLoans(MemberID)
        displayData(data, Books)

        BookID = input('Please enter the ID of the book being returned: ')
        BookLoans.deleteLine(BookID, MemberID)
        print(Books.fields[4])


def main():
        # run below lines to reinitialise the database
        # Books, Members, BookLoans = initialise_databases()
        # delete_all_tables(Books, Members, BookLoans)
        # Books, Members, BookLoans = initialise_databases()
        # input_dummy_data(Books, Members, BookLoans)

        Books, Members, BookLoans = initialise_databases()
        run_UI(Books, Members, BookLoans)


if __name__ == "__main__":
        main()
