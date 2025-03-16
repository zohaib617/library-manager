import json 
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file,'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file,'w') as file:
        json.dump(library, file)

def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').lower() == 'yes'

    new_book = {
        'title' : title,
        'author' : author,
        'year' : year,
        'genre' : genre,
        'read' : read
    }

    library.append(new_book)
    save_library(library)
    print(f'Book {title} added successsfully. ')

def remove_book(library):
    title = input('Enter the title book to remove from the library ')
    initial_legth = len(library)
    library = [book for book in library if book ['title'].lower() != title]
    if len(library) < initial_legth:
        save_library(library)
        print(f'Book {title} removed successfully ')
    else :
        print(f'Book {title} not found in library. ')

def search_library(library):
    search_term = input("Enter book title or author: ").strip().lower()

    results = [book for book in library if 
               ('title' in book and search_term in book['title'].lower()) or 
               ('author' in book and search_term in book['author'].lower())]

    if results:
        for book in results:
            status = 'Read' if book['read'] else 'Unread'
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f"No books found matching '{search_term}'.")


def display_all_books(library):
    if library:
        for book in library:
            status = 'Read' if book['read'] else 'unread'
            print(f"{book[ 'title']} by {book['author']} - {book['year']} - {book['genre']} - {status} ")
    else :
        print('Thi Librari is empty .')

def displahy_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book ['read']])
    percantage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f'Total books: {total_books}')
    print(f'Percantage read : {percantage_read:.2f}%')

def main():
    library = load_library()
    while True:
        print('Welcome to your Persnol Library Manaher! ')
        print('1. Add a book')
        print('2. Remove a book')
        print('3. Search for a book')
        print('4. Display all books')
        print('5. Display statistics ')
        print('6. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == '5':
            displahy_statistics(library)
        elif choice == '6':
            print('Exiting ... Good bye!')
            break
        else :
            print('Invalid choice. Please try again!')

if __name__ == '__main__':
    main()

