from database_creator import DataBase


def initialise_databases():
        Books = DataBase('Books', ['BookId', 'Title', 'Author'], ['INTEGER PRIMARY KEY AUTOINCREMENT', 'TEXT', 'TEXT'])
        Books.createTable()

        BookMembers = DataBase('BookMember', ['BookId', 'MemberID'], ['INTEGER PRIMARY KEY AUTOINCREMENT', 'INTEGER'])
        BookMembers.createTable()

        Members = DataBase('Members', ['MemberId', 'FirstName', 'LastName'], ['INTEGER PRIMARY KEY AUTOINCREMENT', 'TEXT',
                                                                              'TEXT'])
        Members.createTable()

        return Books, Members, BookMembers


def input_dummy_data(Books, Members, BookMembers):
        users = [
                {'FirstName': 'Jane', 'LastName': 'Goodall'},
                {'FirstName': 'Rachel', 'LastName': 'Carson'},
                {'FirstName': 'Barry', 'LastName': 'Bishop'}
                ]

        Members.addData(users)

        books = [
                {'Title': 'The Lord of the Rings', 'Author': 'J.R.R Tolkien'},
                {'Title': 'Harry Potter', 'Author': 'J.K Rowling'},
                {'Title': 'The Colour of Magic', 'Author': 'Terry Pratchett'},
                {'Title': 'The Martian', 'Author': 'Andy Weir'},
                ]

        Books.addData(books)


def delete_all_tables(Books, Members, BookMembers):
        Books.destroyTable()
        Members.destroyTable()
        BookMembers.destroyTable()


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


def run_UI(Books, Members, BookMembers):
        Run = True
        while Run:
                User_Input = input(f'\nWelcome to the Library'
                                   f'\n1: See Books in the Database'
                                   f'\n2: See Library Members in the Database'
                                   f'\n3: Add a new Book to the Database'
                                   f'\n4: Edit the Details of an Existing Book in the Database'
                                   f'\n5: Add a new Member to the Database'
                                   f'\n6: Edit the Details of an Existing Library Member in the Database'
                                   f'\nPlease Make Your Entry: ')

                if User_Input == 'Quit':
                        Run = False
                        break

                elif User_Input == '1':
                        Book_data = Books.getAllData()
                        displayData(Book_data, Books)

                elif User_Input == '2':
                        Member_data = Members.getAllData()
                        displayData(Member_data, Members)

                elif User_Input == '3':
                        books = query_user_4_input(Books)
                        Books.addData(books)
                        print('Thanks, book added')

                elif User_Input == '4':
                        edit_entry(Books)
                        print('Book edited')

                elif User_Input == '5':
                        members = query_user_4_input(Members)
                        Members.addData(members)
                        print('Thanks, new library member added')

                elif User_Input == '6':
                        edit_entry(Members)
                        print('Library member edited')


def edit_entry(Books):
        BookID = input(f'Please enter the {Books.fields[0]} of the Book that you are searching for: ')
        data = Books.findMatchingID(BookID)
        displayData(data, Books)

        user_edit = {}
        for i in range(1, len(Books.fields)):
                User_Edit = input(f'\nEnter new {Books.fields[i]}: ')
                user_edit[f'{Books.fields[i]}'] = User_Edit
        Books.editData(user_edit, BookID)


def main():
        # Books, Members, BookMembers = initialise_databases()
        # delete_all_tables(Books, Members, BookMembers)

        Books, Members, BookMembers = initialise_databases()
        # input_dummy_data(Books, Members, BookMembers)

        run_UI(Books, Members, BookMembers)


if __name__ == "__main__":
        main()
