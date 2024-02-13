class Library:
    # no_of_books = 0
    # books_name = []
    def __init__(self):
        self.no_of_books = 0
        self.books_name = []
        # self.books_name.append(name)
        # self.no_of_books = self.no_of_books + 1
    
    def add_book(self, name):
        self.books_name.append(name)
        self.no_of_books = len(self.books_name)

    def double_checking_the_books(self):
        count = len(self.books_name)
        if(count is self.no_of_books):
            print(F'both the counter of books and lists of the books MATCHES, {count}\n The Total Books in the Library are {count}')
            for book in self.books_name:
                print(book)
        else:
            print('your program is running annonamouly')
    
B1 = Library()
B1.add_book('harry potter1')
B1.add_book('harry potter2')
B1.add_book('harry potter3')
B1.add_book('harry potter4')
print(B1.books_name)
print(B1.no_of_books)
B1.double_checking_the_books()

# B2 = Library()
# B2.add_book('haary potter 2')
# print(B2.books_name)
# print(B2.no_of_books)
# B2.double_checking_the_books()


# B3 = Library('haary potter 3')
# # print(B3.books_name)
# print(B3.no_of_books)
# B3.double_checking_the_books() 


# B4 = Library('haary potter 4')
# # print(B4.books_name)
# print(B4.no_of_books)
# B4.double_checking_the_books()


# B5 = Library('haary potter 5')
# print(B5.books_name)
# print(B5.no_of_books)
# B5.double_checking_the_books()