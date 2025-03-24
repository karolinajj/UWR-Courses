#Karolina Jędraszek
#lista11, zadanie 1
from sqlalchemy.orm import DeclarativeBase, validates, sessionmaker, relationship, mapped_column, Mapped
from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine, select
import sys
from typing import List
import getopt

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "Books"
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String)
    author = relationship("Author", back_populates="books")
    author_id: Mapped[Integer] = Column(ForeignKey("Authors.id"))
    year = mapped_column(Integer)
    borrowed_by = relationship("Friend", back_populates="borrowed_books")
    borrowed_by_id: Mapped[Integer] = Column(ForeignKey("Friends.id"))

    def __init__(self, id, title, author_id, year):
        self.id = id
        self.title = title 
        self.author_id = author_id
        self.year = year
    
    def __repr__(self):
        tmp = f"{self.id}: {self.title}, {self.author_id}, {self.year}"
        if self.borrowed_by != None:
            return f"{tmp}, borrowed by {self.borrowed_by}"
        else: return tmp
    
    @validates("year")
    def validate_year(self, key, year):
        if int(year) < 0:
            raise ValueError("Invalid Year. Year must be greater than 0.")
        return year

class Author(Base):
    __tablename__ = "Authors"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    surname = mapped_column(String)
    books: Mapped[List["Book"]] = relationship("Book", back_populates="author")

    def __init__(self, id, name, surname):
        self.id = id
        self.name = name 
        self.surname = surname

    def __repr__(self):
        return f"{self.id}: {self.name}, {self.surname}"
    
    @validates("surname")
    def validate_surname(self, key, surname):
        for letter in surname:
            if not str.isalpha(letter):
                raise ValueError("Invalid surname. Surname cannot contain characters other than letters.")
        return surname


class Friend(Base):
    __tablename__ = "Friends"
    id = mapped_column(Integer, primary_key=True)
    name  = mapped_column(String)
    email = mapped_column(String)
    borrowed_books: Mapped[List["Book"]] = relationship(back_populates="borrowed_by")

    def __init__(self, id, name, email):
        self.id = id
        self.name = name 
        self.email = email

    def __repr__(self):
        return f"{self.id}: {self.name}, {self.email}"

    @validates("email")
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("Invalid email. Your email must contain '@'")
        return email

def main(argv):
    try:
        opts, arg = getopt.getopt(argv, '', ['add_friend', 'add_author', 'add_book', 'borrow_book', 'return', 'help', 'view_authors', 'view_books', 'view_friends'])
    except getopt.GetoptError:
        print('Invalid command. Type --help for usage instructions.')
        sys.exit(2)

    engine = create_engine("sqlite:///books.db", echo=False)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    if len(arg) == 0 and opts == []:
        print('No arguments and options. Type --help for usage instructions.')
        sys.exit(2)

    opt = opts[0][0]
    if opt == '--help':
        print("""
To add a new book type:
python zad1.py --add_book <id> <"title"> <author's id> <year>
            
To borrow a book type:
python zad1.py --borrow_book <book's id> <friend's id>

To return a book type:
python zad1.py --return <book's id>
        """)
    elif opt == '--add_friend':
        session.add(Friend(*arg))
    elif opt == '--add_author':
        session.add(Author(*arg))
    elif opt == '--add_book':
        session.add(Book(*arg))
    elif opt == '--borrow_book':
        book_id, friend_id = arg
        tmp = select(Book).where(Book.id == book_id)
        book = session.scalars(tmp).one()
        book.borrowed_by_id = friend_id
    elif opt == '--return':
        book_id = arg[0]
        tmp = select(Book).where(Book.id == book_id)
        book = session.scalars(tmp).one()
        book.borrowed_by_id = None
    elif opt =='--view_books':
        books = session.query(Book).all()
        for book in books:
            print(book)
    elif opt =='--view_friends':
        friends = session.query(Friend).all()
        for friend in friends:
            print(friend)
    elif opt =='--view_authors':
        authors = session.query(Author).all()
        for author in authors:
            print(author)

    session.commit()
    session.close()

main(sys.argv[1:])

#python3 zad1.py --add_author 1 Jan Kowalski
#python3 zad1.py --add_author 2 Janina Opolska
#python3 zad1.py --add_author 3 Anna 124
#python3 zad1.py --view_authors

#python3 zad1.py --add_friend 1 Anna anowak@gmail.com
#python3 zad1.py --add_friend 2 Zygmunt znowak@gmail.com
#python3 zad1.py --add_friend 3 Anna a
#python3 zad1.py --view_friends

#python3 zad1.py --add_book 1 "Niebo i morze" 1 2003
#python3 zad1.py --add_book 2 "Niebo i morze cz.2" 1 2004
#python3 zad1.py --add_book 3 Czas 2 1999
#python3 zad1.py --add_book 4 Zapomnienie 2 -9
#python3 zad1.py --view_books

#python3 zad1.py --borrow_book 2 1
#python3 zad1.py --return 2
