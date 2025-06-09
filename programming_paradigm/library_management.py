#!/usr/bin/env python3

class LibraryManagement:
    """A class to manage a library's books and members."""

    def __init__(self):
        """Initialize the library management system."""
        self.books = {}  
        self.members = {}  
        self.next_book_id = 1
        self.next_member_id = 1

    def add_book(self, title, author):
        """
        Add a new book to the library.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            
        Returns:
            int: The ID of the newly added book
        """
        book_id = self.next_book_id
        self.books[book_id] = {
            'title': title,
            'author': author,
            'available': True
        }
        self.next_book_id += 1
        return book_id

    def add_member(self, name):
        """
        Add a new member to the library.
        
        Args:
            name (str): The name of the member
            
        Returns:
            int: The ID of the newly added member
        """
        member_id = self.next_member_id
        self.members[member_id] = {
            'name': name,
            'borrowed_books': []
        }
        self.next_member_id += 1
        return member_id

    def borrow_book(self, book_id, member_id):
        """
        Allow a member to borrow a book.
        
        Args:
            book_id (int): The ID of the book to borrow
            member_id (int): The ID of the member borrowing the book
            
        Returns:
            bool: True if the book was successfully borrowed, False otherwise
        """
        if book_id not in self.books or member_id not in self.members:
            return False

        if not self.books[book_id]['available']:
            return False

        if book_id in self.members[member_id]['borrowed_books']:
            return False

        self.books[book_id]['available'] = False
        self.members[member_id]['borrowed_books'].append(book_id)
        return True

    def return_book(self, book_id, member_id):
        """
        Allow a member to return a book.
        
        Args:
            book_id (int): The ID of the book to return
            member_id (int): The ID of the member returning the book
            
        Returns:
            bool: True if the book was successfully returned, False otherwise
        """
        if book_id not in self.books or member_id not in self.members:
            return False

        if book_id not in self.members[member_id]['borrowed_books']:
            return False

        self.books[book_id]['available'] = True
        self.members[member_id]['borrowed_books'].remove(book_id)
        return True

    def get_book_info(self, book_id):
        """
        Get information about a specific book.
        
        Args:
            book_id (int): The ID of the book
            
        Returns:
            dict: Book information or None if book doesn't exist
        """
        return self.books.get(book_id)

    def get_member_info(self, member_id):
        """
        Get information about a specific member.
        
        Args:
            member_id (int): The ID of the member
            
        Returns:
            dict: Member information or None if member doesn't exist
        """
        return self.members.get(member_id)

    def list_available_books(self):
        """
        Get a list of all available books.
        
        Returns:
            list: List of available book IDs
        """
        return [book_id for book_id, book in self.books.items() if book['available']]

    def list_borrowed_books(self, member_id):
        """
        Get a list of books borrowed by a specific member.
        
        Args:
            member_id (int): The ID of the member
            
        Returns:
            list: List of borrowed book IDs or None if member doesn't exist
        """
        if member_id not in self.members:
            return None
        return self.members[member_id]['borrowed_books']


def main():
    library = LibraryManagement()

    book1_id = library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    book2_id = library.add_book("1984", "George Orwell")
    book3_id = library.add_book("To Kill a Mockingbird", "Harper Lee")

    member1_id = library.add_member("John Doe")
    member2_id = library.add_member("Jane Smith")

    print("Borrowing books...")
    print(f"John borrowing The Great Gatsby: {library.borrow_book(book1_id, member1_id)}")
    print(f"Jane borrowing 1984: {library.borrow_book(book2_id, member2_id)}")
    print(f"John trying to borrow 1984: {library.borrow_book(book2_id, member1_id)}")  # Should fail

    print("\nReturning books...")
    print(f"John returning The Great Gatsby: {library.return_book(book1_id, member1_id)}")
    print(f"Jane returning 1984: {library.return_book(book2_id, member2_id)}")

    print("\nAvailable books:", library.list_available_books())

    print("\nJohn's borrowed books:", library.list_borrowed_books(member1_id))
    print("Jane's borrowed books:", library.list_borrowed_books(member2_id))


if __name__ == "__main__":
    main()