class Book:  
   def __init__(self, title, author, genre, publication_date):  
      self.__title = title  
      self.__author = author  
      self.__genre = genre  
      self.__publication_date = publication_date  
      self.__availability_status = "Available"  
  
   def get_title(self):  
      return self.__title  
  
   def get_author(self):  
      return self.__author  
  
   def get_genre(self):  
      return self.__genre  
  
   def get_publication_date(self):  
      return self.__publication_date  
  
   def get_availability_status(self):  
      return self.__availability_status  
  
   def set_availability_status(self, status):  
      self.__availability_status = status  
  
  
class User:  
   def __init__(self, name, library_id):  
      self.__name = name  
      self.__library_id = library_id  
      self.__borrowed_books = []  
  
   def get_name(self):  
      return self.__name  
  
   def get_library_id(self):  
      return self.__library_id  
  
   def get_borrowed_books(self):  
      return self.__borrowed_books  
  
   def add_borrowed_book(self, book_title):  
      self.__borrowed_books.append(book_title)  
  
   def remove_borrowed_book(self, book_title):  
      self.__borrowed_books.remove(book_title)  
  
  
class Author:  
   def __init__(self, name, biography):  
      self.__name = name  
      self.__biography = biography  
  
   def get_name(self):  
      return self.__name  
  
   def get_biography(self):  
      return self.__biography