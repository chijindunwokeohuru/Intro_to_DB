class Book:
    """
    A class representing a book with title, author, and publication year.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        year (int): The publication year of the book
    """
    
    def __init__(self, title, author, year):
        """
        Initialize a new Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor method called when the object is about to be destroyed.
        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        Return a user-friendly string representation of the book.
        
        Returns:
            str: A formatted string with book information
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Return a developer-friendly string representation of the book.
        
        Returns:
            str: A string that could be used to recreate the object
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"