import unittest
from boggle_solver import Boggle


class TestBoggleSolver(unittest.TestCase):
    """Test suite for Boggle solver"""

    def test_normal_case_with_valid_words(self):
        """Test 1: Normal case - valid grid and dictionary should find words"""
        grid = [["T", "W", "Y", "R"],
                ["E", "N", "P", "H"],
                ["G", "St", "Qu", "R"],
                ["O", "N", "T", "A"]]
        dictionary = ["art", "ego", "gent", "get", "net", "new", "newt",
                     "prat", "pry", "qua", "quart", "rat", "tar", "tarp",
                     "ten", "went", "wet"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("art", result)
        self.assertIn("quart", result)
        self.assertEqual(result, sorted(result))  # Check if sorted

    def test_empty_dictionary(self):
        """Test 2: Empty dictionary should return empty list"""
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)

    def test_empty_grid(self):
        """Test 3: Empty grid should return empty list"""
        grid = []
        dictionary = ["abc", "def", "ghi"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        self.assertEqual(result, [])

    def test_non_square_grid(self):
        """Test 4: Non-square grid should return empty list"""
        grid = [["A", "B", "C"], ["D", "E"]]  # 3x2 - not square
        dictionary = ["abc", "def"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertEqual(result, [])

    def test_dictionary_with_short_words(self):
        """Test 5: Dictionary with words < 3 characters should filter them out"""
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["a", "ab", "abc", "bed", "fed"]  # a, ab should be filtered

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        # Only words >= 3 chars should be found
        for word in result:
            self.assertGreaterEqual(len(word), 3)

    def test_no_matching_words(self):
        """Test 6: Grid with no matching words should return empty list"""
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["xyz", "qwerty", "hello"]  # None of these exist in grid

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertEqual(result, [])

    def test_special_tiles(self):
        """Test 7: Grid with special tiles (Qu, St, Ie) should work correctly"""
        grid = [["T", "W", "Y", "R"],
                ["E", "N", "P", "H"],
                ["G", "St", "Qu", "R"],
                ["O", "N", "T", "A"]]
        dictionary = ["qua", "quart", "stent"]  # Words using special tiles

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        # Should find words with special tiles
        self.assertIn("qua", result)
        self.assertIn("quart", result)

    def test_case_insensitivity(self):
        """Test 8: Mixed case input should be handled (converted to lowercase)"""
        grid = [["A", "R", "T"],
                ["E", "G", "O"],
                ["N", "E", "T"]]
        dictionary = ["ART", "EGO", "NET", "AGE"]  # Uppercase dictionary

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        # Results should be lowercase
        for word in result:
            self.assertEqual(word, word.lower())

    def test_single_cell_grid(self):
        """Test 9: 1x1 grid should return empty list (no 3+ letter words possible)"""
        grid = [["A"]]
        dictionary = ["a", "abc"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertEqual(result, [])

    def test_duplicate_words_filtered(self):
        """Test 10: Same word found via different paths should appear only once"""
        grid = [["A", "R", "T"],
                ["R", "A", "R"],
                ["T", "R", "A"]]
        dictionary = ["art", "rat", "tar"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        # Check no duplicates
        self.assertEqual(len(result), len(set(result)))
        # Check sorted
        self.assertEqual(result, sorted(result))


if __name__ == '__main__':
    unittest.main()
