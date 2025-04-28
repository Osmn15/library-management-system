import datetime
import os

class lms:
    '''
    There are four modules:
    -> add book
    -> return book
    -> borrow book
    -> display book
    '''
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.books_dict = {}
        id = 100
        with open(self.list_of_books) as book:
            content = book.readlines()
        for line in content:
            self.books_dict.update(
                {
                    str(id): {
                        'book_title': line.strip(),
                        'issue_date': '',
                        'lender_name': '',
                        'status': 'available'
                    }
                }
            )
            id += 1  
          
    def display_books(self):
        print('------------------------- List of Books ---------------------------')
        print('Book ID \t\t Book Title')
        for key, value in self.books_dict.items():
            print(key, '\t\t\t', f"{value.get('book_title')}-[{value.get('status')}]")
    def issue_books(self):
        book_id =input('enter book id:')
        currentdate=datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
        if book_id in self.books_dict:
            if self.books_dict[book_id]['status']=='available':
                your_name=input('enter your name:')
                self.books_dict[book_id]['status']='already issued'
                self.books_dict[book_id]['lender_name']=your_name
                self.books_dict[book_id]['issue_date']=currentdate
                print('book issued successfully')
            else:
                print(f"this book {self.books_dict[book_id]['book_title']} is already issued to {self.books_dict[book_id]['lender_name']} on {self.books_dict[book_id]['issue_date']}")
        else:
            print('book id not found')
    def add_books(self):
        new_book = input('Enter book title: ').strip()
        
        if new_book == "":
            print('Book title cannot be empty!')
            return 
        elif len(new_book) > 25:
            print('Book title too long!')
            return  
        else:
            with open(self.list_of_books, 'a') as book:
                book.write(f'{new_book}\n')

            new_id = str(int(max(self.books_dict.keys(), key=int)) + 1)
            
            self.books_dict.update({
                new_id: {
                    "book_title": new_book,
                    'lender_name': '',
                    'issue_date': '',
                    'status': 'available'
                }
            })

            print(f'The book "{new_book}" has been added successfully.')
    def return_book(self):
        book_id=input('enter book your book id')
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]['status']=='available':
                print( f'this {self.books_dict[book_id]['book_title']} book is already in the library')
            else:
                self.books_dict[book_id]['lender_name'] = ""
                self.books_dict[book_id]['issue_date'] = ''
                self.books_dict[book_id]['status'] = 'available'
                print('Book returned successfully and updated.')
        else:
            print('Book ID not found.')
        
#main programm
try:
    mylms=lms('list_of_books.txt','hilal')
    press_key_list = {
        "D": 'Display books',
        "I": 'Issue books',
        "R": 'Return books',
        "A": 'Add books',
        "Q": 'Quit'
    }
    key_press = ""

    while key_press != "q":
        print(f'\n------------------ Welcome to {mylms.library_name} Library Management System ------------------')
        for key, value in press_key_list.items():
            print(f"Press '{key}' to {value}")
        
        key_press = input('Press key: ').lower()

        if key_press == "a":
            print('\nCurrent selection: Add Book\n')
            mylms.add_books()
        elif key_press == "i":
            print('\nCurrent selection: Issue Book\n')
            mylms.issue_books()
        elif key_press == "d":
            print('\nCurrent selection: Display Books\n')
            mylms.display_books()
        elif key_press == "r":
            print('\nCurrent selection: Return Book\n')
            mylms.return_books()
        elif key_press == "q":
            print('Thank you for using the Library Management System!')
            break
        else:
            print('Invalid key! Please try again.')
except Exception as e:
    print('Something went wrong. Please check your input.')
    print('Error:', e)

    