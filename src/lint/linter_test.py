import unittest

from src.lint import linter


lint = lambda fn, suppress=None: list(linter.lint(fn, suppress))


class TestLinter(unittest.TestCase):

    def test_iteritems(self):
        """Test that the linter finds dict.iteritems calls correctly."""
        self.assertEqual([(2, linter.ITERITEMS_USED), (7, linter.ITERITEMS_USED)],
                         lint('src/lint/test_data/test_iteritems'))

    def test_itervalues(self):
        """Test that the linter finds dict.itervalues calls correctly."""
        self.assertEqual([(2, linter.ITERVALUES_USED)], lint('src/lint/test_data/test_itervalues'))

    def test_iterkeys(self):
        """Test that the linter finds dict.iterkeys calls correctly."""
        self.assertEqual([(2, linter.ITERKEYS_USED)], lint('src/lint/test_data/test_iterkeys'))

    def test_syntax_error(self):
        """Test that we handle a syntax error gracefully."""
        self.assertEqual([(4, linter.SYNTAX_ERROR)], lint('src/lint/test_data/test_syntax_error'))

    def test_suppressions(self):
        """Test errors are suppressed correctly."""
        self.assertEqual([(6, linter.ITERITEMS_USED), (9, linter.ITERKEYS_USED)],
                         lint('src/lint/test_data/test_suppressions'))

    def test_unsorted_iteration(self):
        """Test unsorted iteration of set() and dict()."""
        self.assertEqual([(1, linter.UNSORTED_SET_ITERATION), (3, linter.UNSORTED_DICT_ITERATION),
                          (14, linter.UNSORTED_SET_ITERATION), (16, linter.UNSORTED_DICT_ITERATION),
                          (20, linter.UNSORTED_SET_ITERATION), (22, linter.UNSORTED_DICT_ITERATION)],
                         lint('src/lint/test_data/test_unsorted_iteration'))

    def test_non_keyword_calls(self):
        """Test detection of builtin functions being called without keywords."""
        self.assertEqual([(2, linter.NON_KEYWORD_CALL), (5, linter.NON_KEYWORD_CALL)],
                         lint('src/lint/test_data/test_non_keyword_calls'))

    def test_deprecated_functions(self):
        """Test detection of deprecated functions."""
        self.assertEqual([(1, linter.DEPRECATED_FUNCTION)],
                         lint('src/lint/test_data/test_deprecated_functions'))

    def test_incorrect_args(self):
        """Test detection of incorrect arguments."""
        self.assertEqual([(7, linter.INCORRECT_ARGUMENT)],
                         lint('src/lint/test_data/test_incorrect_args'))

    def test_incorrect_args(self):
        """Test detection of duplicates in arguments."""
        self.assertEqual([(9, linter.UNNECESSARY_DUPLICATE)],
                         lint('src/lint/test_data/test_duplicate_args'))

    def test_file_suppressions(self):
        """Test suppressing lint warnings for a whole file."""
        self.assertEqual([(5, linter.ITERKEYS_USED)],
                         lint('src/lint/test_data/test_file_suppressions'))
