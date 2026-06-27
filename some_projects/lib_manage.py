
class library:
    def __init__(self, num, books):
        print("Welcome to the school library!")
        self.no_of_books = int(num)
        self.book_list = list(books)
    def info(self):
        non_text_books = [b for b in self.book_list if isinstance(b, int) or isinstance(b, float)]
        if non_text_books:
            print("Please enter proper names for books, not numbers.")
        elif len(self.book_list) == self.no_of_books:
            for i in self.book_list:
                print(i)
            print(f"There are total {self.no_of_books} books")
            print("YAY! You are good to go")
        elif len(self.book_list) < self.no_of_books:
            print('The number entered is greater than the books you wanna read.')
            print("Please try again")
        else:
            print('The number entered is less than the books you wanna read.')
            print("Please try again")

a = library(2, ('harry potter','thumbs up'))
a.info()


