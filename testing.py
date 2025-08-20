from models import Library, Book

def main():
    # create tables
    Library.create_table()
    Book.create_table()

    #print(Library.table)  # []
    #print(Book.table)     # []

    # drop tables
    #Library.drop_table()
    #Book.drop_table()

    #print(Library.table)  # None
    #print(Book.table)     # None

    lib = Library.create(id=1, name="City Library")
    b1 = Book.create(id=101, title="Python 101", library=lib)
    b2 = Book.create(id=102, title="Data Science Handbook", library=lib)

    lib.add_book(b1)
    lib.add_book(b2)

    lib.save()
    b1.save()
    b2.save()

    b1.delete()


    # print current state of tables
    print("Before update:")
    print(Library.table)
    print(Book.table)

    # change object attributes
    #lib.name = "Central Library"
    #b1.title = "Advanced Python 101"

    # call update to persist changes
    #lib.update()
    #b1.update()

    #print("\nAfter update:")
    print(Library.table)
    print(Book.table)

if __name__ == "__main__":
    main()
