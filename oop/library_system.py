class Book:
    """
    Base class representing a book.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
    """
    
    def __init__(self, title, author):
        """
        Initialize a new Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """
        Return a string representation of the book.
        
        Returns:
            str: Book details as a string
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    A class representing an electronic book, inheriting from Book.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        file_size (int): The file size in KB
    """
    
    def __init__(self, title, author, file_size):
        """
        Initialize a new EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        super().__init__(title, author)  # calling the parent class constructor
        self.file_size = file_size
    
    def __str__(self):
        """
        Return a string representation of the ebook.
        
        Returns:
            str: EBook details as a string
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    A class representing a physical printed book, inheriting from Book.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        page_count (int): The number of pages
    """
    
    def __init__(self, title, author, page_count):
        """
        Initialize a new PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages
        """
        super().__init__(title, author)  # calling the parent class constructor
        self.page_count = page_count
    
    def __str__(self):
        """
        Return a string representation of the print book.
        
        Returns:
            str: PrintBook details as a string
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    A class representing a library that manages a collection of books.
    
    Attributes:
        books (list): A list containing Book, EBook, and PrintBook instances
    """
    
    def __init__(self):
        """
        Initialize a new Library instance with an empty book list.
        """
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book: An instance of Book, EBook, or PrintBook
        """
        self.books.append(book)
    
    def list_books(self):
        """
        Print details of all books in the library.
        """
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)