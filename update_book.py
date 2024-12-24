# PROMPT BLACKBOX AI - CLAUDE SONNET 3.5 MODEL
# @Claude-Sonnet-3.5 I have txt file that wrote csv like format. That file contains database of books, that the first index is the title of the book, and the second one is the author of the book, separated with comma like the csv file. I already made code that can add new book into the txt file with csv like format. And also already made code that can delete the book. How can i make the code for update the book? my programming language is python

def update_book(filename):
    # Read the current books
    with open(filename, 'r') as file:
        books = file.readlines()
    
    # Display current books
    print("Current books:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book.strip()}")
    
    # Ask which book to update
    try:
        book_index = int(input("Enter the number of the book you want to update: ")) - 1
        
        # Validate index
        if book_index < 0 or book_index >= len(books):
            print("Invalid book number!")
            return
        
        # Split the current book details
        current_book = books[book_index].strip().split(',')
        
        # Get new details
        print("\nCurrent book details:")
        print(f"Title: {current_book[0]}")
        print(f"Author: {current_book[1]}")
        
        # Ask for new details
        new_title = input("Enter new title (press Enter to keep current): ").strip()
        new_author = input("Enter new author (press Enter to keep current): ").strip()
        
        # Use current details if no new input
        new_title = new_title if new_title else current_book[0]
        new_author = new_author if new_author else current_book[1]
        
        # Create updated book entry
        updated_book = f"{new_title},{new_author}\n"
        
        # Replace the old book with the updated one
        books[book_index] = updated_book
        
        # Write back to file
        with open(filename, 'w') as file:
            file.writelines(books)
        
        print("Book updated successfully!")
    
    except ValueError:
        print("Please enter a valid number!")

# Example usage
filename = 'books_database.txt'
update_book(filename)