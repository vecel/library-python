from library import Book, Library

LIBRARY_FILE_NAME = 'library.txt'

library = Library()

def load():
    '''Open library file and load its content'''
    
    def create_book(properties: list) -> Book :
        id      = int(properties[0])
        title   =     properties[1]
        author  =     properties[2]
        status  =     properties[3]
        rating  = int(properties[4])
        country = properties[5]
        return Book(id, title, author, status, rating, country)



    lib = open(LIBRARY_FILE_NAME)

    # skip first line
    lib.readline()

    for record in lib.readlines():
        b = create_book(record.split(';'))
        library.add(b)
        
    lib.close()

def run():
    '''Operate on library data'''
    pass

def close():
    '''Save changes to library file
    
    This function clears and rewrites library file'''
    pass

load()
library.print_catalog()