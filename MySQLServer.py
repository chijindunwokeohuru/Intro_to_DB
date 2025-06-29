

import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Creates the alx_book_store database in MySQL server
    Handles connection, creation, and proper closure
    """
    connection = None
    cursor = None
    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='' 
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)
            
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()

