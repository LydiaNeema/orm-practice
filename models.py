class Library:
    table = []
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def add_book(self,book):
        book.library = self
        self.table.append(book)
    @classmethod
    def create_table(cls):
        cls.table = []
        print("Table 'libraries' created.")   
    @classmethod
    def drop_table(cls):
        cls.table = None 
        print("Table 'libraries' dropped.") 

    def save(self):
        """Save this object as a row in the table"""
        row = {
            "id": self.id,
            "name": self.name
        }
        self.__class__.table.append(row)
        print(f"Saved {self} to table.") 
    def update(self):
        """Update this object's row in the table"""
        for row in self.__class__.table:
            if row["id"] == self.id:
               row["name"] = self.name   # update changed field
            print(f"Updated {self} in table.")
            break    
    def delete(self):
        """Delete this object's row from the table"""
        for row in self.__class__.table:
           if row["id"] == self.id:
            self.__class__.table.remove(row)
            print(f"Deleted {self} from table.")
            break
      
    @classmethod
    def create(cls, **attributes):
       """Create a new object and save it in the table"""
       obj = cls(**attributes)  # make instance
       obj.save()               # save to table
       return obj               # return the instance

class Book:
    table = [] #create a class variable to hold all book instances
    def __init__(self,id,title,library=None):
        self.id = id
        self.title = title
        self.library = library
    @classmethod
    def create_table(cls):
        cls.table = []
        print("Table 'books' created.")   
    @classmethod
    def drop_table(cls):
        cls.table = None 
        print("Table 'books' dropped.") 
    def save(self):
        """Save this object as a row in the table"""
        row = {
            "id": self.id,
            "title": self.title,
            "library_id": self.library.id if self.library else None
        }
        self.__class__.table.append(row)
        print(f"Saved {self} to table.") 
    def update(self):
        """Update this object's row in the table"""
        for row in self.__class__.table:
            if row["id"] == self.id:
               row["title"] = self.title
               row["library_id"] = self.library.id if self.library else None
            print(f"Updated {self} in table.")
            break
    def delete(self):
        """Delete this object's row from the table"""
        for row in self.__class__.table:
            if row["id"] == self.id:
               self.__class__.table.remove(row)
               print(f"Deleted {self} from table.")
               break
    
      
    @classmethod
    def create(cls, **attributes):
        obj = cls(**attributes)
        obj.save()
        return obj
    

    def __repr__(self) :
        return f"<Book id={self.id} title='{self.title}'>"