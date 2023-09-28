# Online Book Reader: Design the data structures for an online book reader system

# Only one active user with only one active book

# Main Class: OnlineReader: accesses other classes.
# Classes: Library, UserManager, Display, Basic Classes: Book, User

class OnlineReader:
    def __init__(self):
        self.user_manager = UserManager()
        self.library = Library()
        self.display = Display()

        self.book = Book()
        self.active_user = User()

    def set_active_book(self, book):
        self.book = book
        self.display.display_book(book)
    
    def set_active_user(self, user):
        self.active_user = user
    
    # Also define getters for each class instanct here.

class Library:
    def __init__(self):
        self.book_list = {} # ID -> Book

    def add_book(self, id, details):
        if id not in self.book_list:
            self.book_list[id] = Book(id, details)
            return self.book_list[id]
        return None
    
    def remove_book(self, id = 0, book: Book):
        if not id:
            id = book.id
        if id not in self.book_list:
            return False
        self.book_list.pop(id)
        return True

    def find_book(self, id):
        if id in self.book_list:
            return self.book_list[id]
        
class UserManager:
    def __init__(self):
        self.users = {}
    
    def add_user(self, id,details):
        if id not in self.users:
            self.users[id] = ((id, details))
        return self.users[id]
    
    def remove_user(self, id):
        pass

    def find_user_by_details(self, details):
        pass

class Display:
    def __init__(self):
        self.page_number = 0
        self.active_book = None
        self.active_user = None

    def display_book(self,book):
        self.page_number = 0
        self.active_book = book
        # Code to refresh the actual display

    def page_forward(self):
        pass
    def page_backward(self):
        pass


class Book:
    def __init__(self,id,details):
        self.book_id = id
        self.details = details

    # Getter-Setter functions

class User:
    def __init__(self, id, details):
        self.user_id = id
        self.user_details = details

    # Details is ambiguous here and substitutes any other information such as membership details, credit card details, book progress etc.

    
        