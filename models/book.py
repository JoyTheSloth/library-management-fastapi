class Book:
    def __init__(self, book_id: int ,title : str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
        
    def issue(self):
        if not self.available:
            raise Exception("Book is already issued")
        self.available = False
        
    def return_book(self):
        self.available = True