
import json
import os

data_file = "library.txt"

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').strip().lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f'\n📚 Book "{title}" added successfully!')

def remove_book(library):
    title = input("Enter the title of the book to remove from the library: ").lower()
    new_library = [book for book in library if book['title'].lower() != title]

    if len(new_library) < len(library):
        save_library(new_library)
        print(f'\n🗑️ Book "{title}" removed successfully.')
        return new_library
    else:
        print(f'\n❌ Book "{title}" not found in the library.')
        return library

def search_library(library):
    search_by = input('Search by "title" or "author": ').strip().lower()
    if search_by not in ['title', 'author']:
        print(" Invalid search type.")
        return

    search_term = input(f"Enter the {search_by}: ").strip().lower()
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        print(f"\n Found {len(results)} matching book(s):\n")
        for book in results:
            status = "Read" if book['read'] else 'Unread'
            print(f" {book['title']} by {book['author']} | {book['year']} | {book['genre']} | {status}")
    else:
        print(f"\n No books found matching '{search_term}' in the {search_by} field.")

def main():
    library = load_library()
    while True:
        print("\n========== Library Manager ==========")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Library")
        print("4. Exit")
        print("=====================================")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            library = remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
