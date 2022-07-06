from library import Book, Library

def load(library: Library, filename: str):
    '''Load contents of library database from txt file to library object.
    
    Arguments:
    library - Library object to be loaded
    filename - txt file that contains library data'''

    NO_FILE_MSG      = f'Cannot find {filename}, Library not loaded.'    
    ASK_MSG          = f'Do you want to create {filename} file? [y/n]\n'
    INIT_DB_TEXT     = 'id;title;author;status;rating;country;\n'
    DB_CREATED_MSG = f'Database {filename} succesfully created!'

    def fetch_book(properties: list) -> Book :
        id      = int(properties[0])
        title   =     properties[1]
        author  =     properties[2]
        status  =     properties[3]
        rating  = int(properties[4])
        country = properties[5]
        return Book(id, title, author, status, rating, country)

    def create_database(db_name: str):
        with open(db_name, 'x') as db:
            db.write(INIT_DB_TEXT)

        print(DB_CREATED_MSG)

    try:
        lib_DB = open(filename, 'r')
    except:
        print(NO_FILE_MSG)

        ans = input(ASK_MSG).lower()
        if ans == 'y':
            create_database(filename)
        
        return

    # skip first line
    lib_DB.readline()

    for record in lib_DB.readlines():
        b = fetch_book(record.split(';'))
        library.add(b)
        
    lib_DB.close()

def run(library: Library):
    '''Operate on library data.
    
    Arguments:
    library - Library object to be operated with'''
    pass

def save(library: Library, filename: str):
    '''Save changes made in library to txt file.
    
    This function clears and rewrites database (txt) file.
    
    Arguments:
    library - Library object to be saved
    filename - txt file to store saved data'''
    pass


LIBRARY_FILE_NAME = 'library.txt'

library = Library()

load(library, 'library.txt')
library.display_catalog()