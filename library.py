class Book:
    def __init__(self, id: int, title: str, author: str, status: str, rating: int, country: str):
        self.id = id
        self.title = title
        self.author = author
        self.status = status
        self.rating = rating
        self.country = country

    def print_properties(self):
        print(self.id, self.title, self.author, self.status, self.rating, self.country)


class Library:
    def __init__(self):
        self.books = None

    def add(self, book: Book):
        if self.books is None:
            self.books = []
        self.books.append(book)

    def print_catalog(self):
        for b in self.books:
            b.print_properties()