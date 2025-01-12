```python
# Book Recommendation System

# Create a dictionary of books and their corresponding genres
books = {
    'Book1': 'Mystery',
    'Book2': 'Romance',
    'Book3': 'Sci-Fi',
    'Book4': 'Fiction',
    'Book5': 'Fantasy'
}

# Function that recommends books based on user's genre preferences
def recommend_books(genre):
    recommended_books = [book for book, book_genre in books.items() if book_genre == genre]
    return recommended_books

# Main program
print("Welcome to the Book Recommendation System!")
print("Genres available: Mystery, Romance, Sci-Fi, Fiction, Fantasy")

# Get user input for genre preference
while True:
    try:
        genre = input("Enter your preferred genre: ").capitalize()
        if genre in books.values():
            recommended_books = recommend_books(genre)
            print(f"Here are some books in the {genre} genre:")
            for book in recommended_books:
                print(book)
            break
        else:
            print("Invalid genre. Please try again.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
```

This program creates a book recommendation system where the user can input their preferred genre, and the program will recommend books in that genre. Error handling is included to handle invalid inputs and user interruption.