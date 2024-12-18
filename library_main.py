import library_class
import library_data  
  
def display_main_menu():  
   print("Welcome to the Library Management System!")  
   print("Main Menu:")  
   print("1. Book Operations")  
   print("2. User Operations")  
   print("3. Author Operations")  
   print("4. Quit")  
  
def display_book_menu():  
   print("Book Operations:")  
   print("1. Add a new book")  
   print("2. Borrow a book")  
   print("3. Return a book")  
   print("4. Search for a book")  
   print("5. Display all books")  
  
def display_user_menu():  
   print("User Operations:")  
   print("1. Add a new user")  
   print("2. View user details")  
   print("3. Display all users")  
  
def display_author_menu():  
   print("Author Operations:")  
   print("1. Add a new author")  
   print("2. View author details")  
   print("3. Display all authors")  
  
def add_book():  
   title = input("Enter book title: ")  
   author = input("Enter book author: ")  
   genre = input("Enter book genre: ")  
   publication_date = input("Enter book publication date: ")  
   new_book = library_class.Book(title, author, genre, publication_date)  
   library_data.add_book(new_book)  
  
def borrow_book():  
   title = input("Enter book title: ")  
   book = library_data.get_book(title)  
   if book and book.get_availability_status() == "Available":  
      book.set_availability_status("Borrowed")  
      user_id = input("Enter user ID: ")  
      user = library_data.get_user(user_id)  
      if user:  
        user.add_borrowed_book(title)  
        print("Book borrowed successfully!")  
      else:  
        print("User not found!")  
   else:  
      print("Book not available or not found!")  
  
def return_book():  
   title = input("Enter book title: ")  
   book = library_data.get_book(title)  
   if book and book.get_availability_status() == "Borrowed":  
      book.set_availability_status("Available")  
      user_id = input("Enter user ID: ")  
      user = library_data.get_user(user_id)  
      if user and title in user.get_borrowed_books():  
        user.remove_borrowed_book(title)  
        print("Book returned successfully!")  
      else:  
        print("User not found or book not borrowed!")  
   else:  
      print("Book not borrowed or not found!")  
  
def search_book():  
   title = input("Enter book title: ")  
   book = library_data.get_book(title)  
   if book:  
      print("Book Title:", book.get_title())  
      print("Book Author:", book.get_author())  
      print("Book Genre:", book.get_genre())  
      print("Book Publication Date:", book.get_publication_date())  
      print("Book Availability Status:", book.get_availability_status())  
   else:  
      print("Book not found!")  
  
def display_books():  
   books = library_data.get_all_books()  
   for book in books:  
      print("Book Title:", book.get_title())  
      print("Book Author:", book.get_author())  
      print("Book Genre:", book.get_genre())  
      print("Book Publication Date:", book.get_publication_date())  
      print("Book Availability Status:", book.get_availability_status())  
      print("------------------------")  
  
def add_user():  
   name = input("Enter user name: ")  
   library_id = input("Enter user library ID: ")  
   new_user = library_class.User(name, library_id)  
   library_data.add_user(new_user)  
  
def view_user():  
   user_id = input("Enter user ID: ")  
   user = library_data.get_user(user_id)  
   if user:  
      print("User Name:", user.get_name())  
      print("User Library ID:", user.get_library_id())  
      print("Borrowed Books:", user.get_borrowed_books())  
   else:  
      print("User not found!")  
  
def display_users():  
   users = library_data.get_all_users()  
   for user in users:  
      print("User Name:", user.get_name())  
      print("User Library ID:", user.get_library_id())  
      print("Borrowed Books:", user.get_borrowed_books())  
      print("------------------------")  
  
def add_author():  
   name = input("Enter author name: ")  
   biography = input("Enter author biography: ")  
   new_author = library_class.Author(name, biography)  
   library_data.add_author(new_author)  
  
def view_author():  
   name = input("Enter author name: ")  
   author = library_data.get_author(name)  
   if author:  
      print("Author Name:", author.get_name())  
      print("Author Biography:", author.get_biography())  
   else:  
      print("Author not found!")  
  
def display_authors():  
   authors = library_data.get_all_authors()  
   for author in authors:  
      print("Author Name:", author.get_name())  
      print("Author Biography:", author.get_biography())  
      print("------------------------")  
  
def main():  
   while True:  
      display_main_menu()  
      choice = input("Enter your choice: ")  
      if choice == "1":  
        while True:  
           display_book_menu()  
           book_choice = input("Enter your choice: ")  
           if book_choice == "1":  
              add_book()  
           elif book_choice == "2":  
              borrow_book()  
           elif book_choice == "3":  
              return_book()  
           elif book_choice == "4":  
              search_book()  
           elif book_choice == "5":  
              display_books()  
           else:  
              print("Invalid choice!")  
              break  
      elif choice == "2":  
        while True:  
           display_user_menu()  
           user_choice = input("Enter your choice: ")  
           if user_choice == "1":  
              add_user()  
           elif user_choice == "2":  
              view_user()  
           elif user_choice == "3":  
              display_users()  
           else:  
              print("Invalid choice!")  
              break  
      elif choice == "3":  
        while True:  
           display_author_menu()  
           author_choice = input("Enter your choice: ")  
           if author_choice == "1":  
              add_author()  
           elif author_choice == "2":  
              view_author()  
           elif author_choice == "3":  
              display_authors()  
           else:  
              print("Invalid choice!")  
              break  
      elif choice == "4":  
        print("Goodbye!")  
        break  
      else:  
        print("Invalid choice!")  
  
if __name__ == "__main__":  
   main()