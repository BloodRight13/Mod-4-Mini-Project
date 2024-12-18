import library_class  
  
books = []  
users = []  
authors = []  
  
def add_book(book):  
   books.append(book)  
  
def get_book(title):  
   for book in books:  
      if book.get_title() == title:  
        return book  
   return None  
  
def get_all_books():  
   return books  
  
def add_user(user):  
   users.append(user)  
  
def get_user(library_id):  
   for user in users:  
      if user.get_library_id() == library_id:  
        return user  
   return None  
  
def get_all_users():  
   return users  
  
def add_author(author):  
   authors.append(author)  
  
def get_author(name):  
   for author in authors:  
      if author.get_name() == name:  
        return author  
   return None  
  
def get_all_authors():  
   return authors