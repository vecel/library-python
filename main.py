from library import Book, Library

def load(library: Library, filename: str):
    '''Load contents of library database from txt file to library object
    
    Arguments:
    library - Library object to be loaded
    filename - txt file that contains library data'''
    
    def create_book(properties: list) -> Book :
        id      = int(properties[0])
        title   =     properties[1]
        author  =     properties[2]
        status  =     properties[3]
        rating  = int(properties[4])
        country = properties[5]
        return Book(id, title, author, status, rating, country)


    try:
        lib_DB = open(filename)
    except:
        print(f'Cannot find {filename}, Library not loaded.')
        return

    # skip first line
    lib_DB.readline()

    for record in lib_DB.readlines():
        b = create_book(record.split(';'))
        library.add(b)
        
    lib_DB.close()

def run():
    '''Operate on library data'''
    pass

def close():
    '''Save changes to library file
    
    This function clears and rewrites library file'''
    pass


LIBRARY_FILE_NAME = 'library.txt'

library = Library()

load(library, LIBRARY_FILE_NAME)
library.display_catalog()