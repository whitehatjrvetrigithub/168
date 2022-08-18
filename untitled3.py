class BookShelf:
    
    def __init__(self, name, author, price, pub_yr):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_pub_yr = pub_yr
        
    def add_book(self):
        print("Book Name : " + self.book_name)
        print("Book Author : " + self.book_author)
        print("Book Price : " + str(self.book_price) + "/-")
        print("Book Publishing Year : " + str(self.book_pub_yr))
        print("Book Added")
        
    def yrs_since_pub(self):
        yrs_ago_pub = 2022 - self.book_pub_yr
        print("This Book Was Published " + str(yrs_ago_pub) + " Years Ago")
        
book1 = BookShelf("Harry Potter & The Philosopher's Stone", "J.K. Rowling", 1928, 1997)
book1.add_book()
book1.yrs_since_pub()

book2 = BookShelf("Diary Of A Wimpy Kid", "Jeff Kinney", 700, 2017)
book2.add_book()
book2.yrs_since_pub()