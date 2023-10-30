import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        book_lover = BookLover()
        book_lover.add_book("Book 1")
        self.assertIn("Book 1", book_lover.book_list)
        print(book_lover)

    def test_2_add_book(self):
        book_lover = BookLover()
        book_lover.add_book("Book 2")
        book_lover.add_book("Book 2")
        self.assertEqual(book_lover.book_list.count("Book 2"), 1)
        print(book_lover)

    def test_3_has_read(self):
        book_lover = BookLover()
        book_lover.add_book("Book 3")
        self.assertTrue(book_lover.has_read("Book 3"))
        print(book_lover)

    def test_4_has_read(self):
        book_lover = BookLover()
        self.assertFalse(book_lover.has_read("Book 4"))
        print(book_lover)

    def test_5_num_books_read(self):
        book_lover = BookLover()
        book_lover.add_book("Book 5")
        book_lover.add_book("Book 6")
        book_lover.add_book("Book 7")
        self.assertEqual(book_lover.num_books_read(), 3)
        print(book_lover)

    def test_6_fav_books(self):
        book_lover = BookLover()
        book_lover.add_book_with_rating("Book 8", 4)
        book_lover.add_book_with_rating("Book 9", 2)
        book_lover.add_book_with_rating("Book 10", 7)
        fav_books = book_lover.get_favorite_books()
        self.assertTrue(all(book[1] > 3 for book in fav_books))
        

if __name__ == '__main':
    unittest.main(verbosity=3)
    
    
    