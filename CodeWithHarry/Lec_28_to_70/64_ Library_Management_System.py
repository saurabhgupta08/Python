class library:
    no_of_books=6
    books=["hindi","Englis","SST","Science","Geo","Maths"]

    
    def add_book(sefl,new_book):
        sefl.books.append(new_book)
        sefl.no_of_books+=1
    def books_info(sefl):
        print("The books are:")
        for i in sefl.books:
            print(i)
        print(f"The number of books is {sefl.no_of_books}")

a=library()
a.add_book("DBMS")
a.add_book("DBMS1")
a.add_book("DBMS2")
a.books_info()     
