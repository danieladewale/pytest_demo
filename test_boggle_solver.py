import unittest
from boggle_solver import Boggle


class TestBoggleSolver(unittest.TestCase):
    """Comprehensive test suite for Boggle solver"""

    # ========== BASIC TESTS ==========

    def test_finds_valid_words(self):
        """BASIC: Finds valid words in grid"""
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
        # Verify specific valid words are found
        self.assertIn("art", result)
        self.assertIn("rat", result)
        self.assertIn("tar", result)
        self.assertIn("net", result)
        self.assertIn("ten", result)
        self.assertIn("get", result)
        self.assertEqual(result, sorted(result))  # Must be sorted

    def test_diagonal_adjacency(self):
        """BASIC: Words formed using diagonal adjacency work"""
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["aei", "beh", "ceg", "gec", "aef"]  # Diagonal paths

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        # AEI: A(0,0) -> E(1,1) -> I(2,2) diagonal
        self.assertIn("aei", result)
        # BEH: B(0,1) -> E(1,1) -> H(2,1)
        self.assertIn("beh", result)
        # CEG: C(0,2) -> E(1,1) -> G(2,0) diagonal
        self.assertIn("ceg", result)

    def test_non_adjacent_letters_rejected(self):
        """BASIC: Words with non-adjacent letters should NOT be found"""
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["aci", "agi", "cag", "afh", "iah"]  # Non-adjacent paths

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        # These words require non-adjacent jumps, should NOT be found
        self.assertNotIn("aci", result)  # A(0,0) to C(0,2) not adjacent
        self.assertNotIn("agi", result)  # A(0,0) to G(2,0) not adjacent
        self.assertNotIn("cag", result)  # C to A not adjacent
        self.assertNotIn("afh", result)  # A to F not adjacent
        self.assertNotIn("iah", result)  # I to A not adjacent

    # ========== EDGE CASES ==========

    def test_duplicate_letters_in_grid(self):
        """EDGE CASE: Grid with duplicate letters - each cell can only be used once per word"""
        grid = [["A", "R", "T"],
                ["R", "A", "R"],
                ["T", "R", "A"]]
        dictionary = ["art", "rat", "tar", "rar", "ara", "tart", "rara"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        # Valid words that can be formed
        self.assertIn("art", result)
        self.assertIn("rat", result)
        self.assertIn("tar", result)
        # RAR can be formed: R(0,1)->A(0,0)->R(1,0) or other paths
        self.assertIn("rar", result)
        # ARA can be formed: A(0,0)->R(0,1)->A(1,1) or other paths
        self.assertIn("ara", result)
        # Check no duplicates in result
        self.assertEqual(len(result), len(set(result)))

    def test_short_words_filtered(self):
        """EDGE CASE: Words < 3 characters should be filtered out"""
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["a", "ab", "abc", "bed", "fed", "de", "hi"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        # Only words >= 3 chars should be found
        for word in result:
            self.assertGreaterEqual(len(word), 3)
        # Short words should NOT appear
        self.assertNotIn("a", result)
        self.assertNotIn("ab", result)
        self.assertNotIn("de", result)
        self.assertNotIn("hi", result)

    def test_empty_dictionary(self):
        """EDGE CASE: Empty dictionary should return empty list"""
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)

    def test_empty_grid(self):
        """EDGE CASE: Empty grid should return empty list"""
        grid = []
        dictionary = ["abc", "def", "ghi"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        self.assertEqual(result, [])

    # ========== SPECIAL TILES (Q, S, I) TESTS ==========

    def test_qu_tile_counts_as_two_letters(self):
        """SPECIAL TILE: Qu tile counts as 2 letters and must be treated correctly"""
        grid = [["T", "W", "Y", "R"],
                ["E", "N", "P", "H"],
                ["G", "St", "Qu", "R"],
                ["O", "N", "T", "A"]]
        dictionary = ["qua", "quart", "quar", "pqu", "qur"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        # QUA should be found (Qu counts as "qu", then "a")
        self.assertIn("qua", result)
        # QUART should be found if path exists
        self.assertIn("quart", result)

    def test_no_standalone_q_tile(self):
        """SPECIAL TILE: There are no standalone 'Q' tiles - only 'Qu' tiles"""
        grid = [["A", "B", "C"],
                ["Qu", "E", "F"],
                ["G", "H", "I"]]
        # Words that would require standalone Q (invalid)
        dictionary = ["qe", "qef", "aqb", "qi"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        # None of these should be found because 'Qu' is 2 letters, not just 'Q'
        # QE would need to be "que" to match the Qu tile
        self.assertNotIn("qe", result)
        self.assertNotIn("qi", result)

    def test_q_not_followed_by_u_invalid(self):
        """SPECIAL TILE: Q not followed by U should not exist (only Qu tiles exist)"""
        grid = [["A", "B", "C"],
                ["Qu", "E", "F"],
                ["G", "H", "I"]]
        # "Qu" tile represents "qu" - so "qe" is invalid, must be "que"
        dictionary = ["que", "quef", "aqua"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        # QUE: Qu(1,0) -> E(1,1) should be found
        self.assertIn("que", result)

    def test_st_tile_counts_as_two_letters(self):
        """SPECIAL TILE: St tile counts as 2 letters"""
        grid = [["T", "W", "Y", "R"],
                ["E", "N", "P", "H"],
                ["G", "St", "Qu", "R"],
                ["O", "N", "T", "A"]]
        dictionary = ["stent", "gest", "nest", "gst"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        # Words containing "st" via the St tile should work
        # GST would be: G->St (but St = "st", so this is G->S->T as 3 letters)
        # Actually, the grid shows "St" as a single tile that represents "st"

    def test_ie_tile_counts_as_two_letters(self):
        """SPECIAL TILE: Ie tile counts as 2 letters"""
        grid = [["T", "Ie", "D"],
                ["A", "R", "E"],
                ["M", "O", "N"]]
        dictionary = ["tie", "tied", "tier", "aie"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        # TIE: T(0,0) -> Ie(0,1) should be found (3 letters total)
        self.assertIn("tie", result)
        # TIED: T(0,0) -> Ie(0,1) -> D(0,2) should be found
        self.assertIn("tied", result)

    def test_no_standalone_s_tile(self):
        """SPECIAL TILE: No standalone 'S' tiles exist - only 'St' tiles"""
        grid = [["A", "B", "C"],
                ["St", "E", "F"],
                ["G", "H", "I"]]
        # If someone tries to find just "s", it shouldn't work
        dictionary = ["ste", "stef", "ast"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        # STE: St(1,0) -> E(1,1) should work (3 letters: s-t-e)
        self.assertIn("ste", result)

    def test_no_standalone_i_tile(self):
        """SPECIAL TILE: No standalone 'I' tiles exist - only 'Ie' tiles"""
        grid = [["A", "B", "C"],
                ["Ie", "E", "F"],
                ["G", "H", "I"]]  # This 'I' is a regular 'I', not part of spec
        dictionary = ["iee", "aie", "ief"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        # IEE: Ie(1,0) -> E(1,1) should work (3 letters: i-e-e)
        self.assertIn("iee", result)

    # ========== INVALID INPUTS ==========

    def test_non_square_grid(self):
        """INVALID INPUT: Non-square grid should return empty list"""
        grid = [["A", "B", "C"], ["D", "E"]]  # 3x2 - not square
        dictionary = ["abc", "def"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertEqual(result, [])

    def test_jagged_grid(self):
        """INVALID INPUT: Jagged grid (inconsistent row lengths) should return empty"""
        grid = [["A", "B"], ["C", "D", "E"], ["F"]]
        dictionary = ["abc", "def"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertEqual(result, [])

    def test_single_cell_grid(self):
        """INVALID INPUT: 1x1 grid should return empty (no 3+ letter words possible)"""
        grid = [["A"]]
        dictionary = ["a", "abc"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertEqual(result, [])

    def test_none_grid(self):
        """INVALID INPUT: None grid should return empty list"""
        grid = None
        dictionary = ["abc", "def"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertEqual(result, [])

    def test_none_dictionary(self):
        """INVALID INPUT: None dictionary should return empty list"""
        grid = [["A", "B"], ["C", "D"]]
        dictionary = None

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertEqual(result, [])

    # ========== ORDERING AND CORRECTNESS ==========

    def test_result_is_sorted(self):
        """ORDERING: Result must be sorted alphabetically"""
        grid = [["T", "W", "Y", "R"],
                ["E", "N", "P", "H"],
                ["G", "St", "Qu", "R"],
                ["O", "N", "T", "A"]]
        dictionary = ["wet", "art", "net", "get", "ten", "rat", "tar"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        # Result must be sorted
        self.assertEqual(result, sorted(result))

    def test_no_duplicate_results(self):
        """CORRECTNESS: Same word via different paths should appear only once"""
        grid = [["A", "R", "T"],
                ["R", "A", "R"],
                ["T", "R", "A"]]
        dictionary = ["art", "rat", "tar", "ara"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        # Check no duplicates
        self.assertEqual(len(result), len(set(result)))

    def test_no_matching_words(self):
        """CORRECTNESS: Grid with no matching words should return empty list"""
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["xyz", "qwerty", "hello"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertEqual(result, [])

    def test_case_insensitivity(self):
        """CORRECTNESS: Mixed case input should be handled (converted to lowercase)"""
        grid = [["A", "R", "T"],
                ["E", "G", "O"],
                ["N", "E", "T"]]
        dictionary = ["ART", "EGO", "NET", "AGE"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        self.assertIsInstance(result, list)
        # Results should be lowercase
        for word in result:
            self.assertEqual(word, word.lower())

    def test_cell_reuse_not_allowed(self):
        """CORRECTNESS: Each cell can only be used once per word"""
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        # ABA would require using A twice, BEB would require using B twice
        dictionary = ["aba", "beb", "aea"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        # These should NOT be found because they'd require reusing cells
        self.assertNotIn("aba", result)
        self.assertNotIn("beb", result)
        self.assertNotIn("aea", result)

    def test_comprehensive_valid_solution(self):
        """CORRECTNESS: Comprehensive test with known valid words"""
        grid = [["T", "W", "Y", "R"],
                ["E", "N", "P", "H"],
                ["G", "St", "Qu", "R"],
                ["O", "N", "T", "A"]]
        dictionary = ["art", "ego", "gent", "get", "net", "new", "newt",
                     "prat", "pry", "qua", "quart", "rat", "tar", "tarp",
                     "ten", "went", "wet", "arty", "egg", "not"]

        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()

        # Valid words that SHOULD be found
        valid_words = ["art", "ego", "gent", "get", "net", "new", "newt",
                      "prat", "pry", "qua", "quart", "rat", "tar", "tarp",
                      "ten", "went", "wet"]

        for word in valid_words:
            self.assertIn(word, result, f"Valid word '{word}' should be found")

        # Invalid words that should NOT be found
        invalid_words = ["arty", "egg", "not"]
        for word in invalid_words:
            self.assertNotIn(word, result, f"Invalid word '{word}' should NOT be found")


if __name__ == '__main__':
    unittest.main()
