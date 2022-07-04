class Book:
    def __init__(self, id: int, title: str, author: str, status: str, rating: int, country: str):
        self.id = id
        self.title = title
        self.author = author
        self.status = status
        self.rating = rating
        self.country = country

    def print_properties(self):
        print(f'{self.id}. {self.title} by {self.author} from {self.country}, status: {self.status}, rating: {self.rating}')


class Library:
    def __init__(self):
        self.books = None

    def add(self, book: Book):
        if self.books is None:
            self.books = []
        self.books.append(book)

    def display_catalog(self):
        for b in self.books:
            b.print_properties()

    def get_book(self, *, id: int = None, title: str = None) -> Book:
        '''Return book with specified id or title, if neither is found return None.
        
        This function takes up to two named arguments: book's id and title'''

        if id == None and title == None:
            return None

        for b in self.books:
            if (id is None or b.id == id) and (title is None or b.title == title):
                return b
        
        return None