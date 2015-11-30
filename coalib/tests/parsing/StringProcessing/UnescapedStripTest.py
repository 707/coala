import sys
import unittest

sys.path.insert(0, ".")
from coalib.tests.parsing.StringProcessing.StringProcessingTestBase import (
    StringProcessingTestBase)
from coalib.parsing.StringProcessing import unescaped_rstrip, unescaped_strip


class UnescapedStripTest(StringProcessingTestBase):
    test_strings2 = ("hello\\",
                     "te\\st\\\\",
                     "A\\ ",
                     "A\\       ",
                     "   A \\ \\  ",
                     "    \\ A \\    ",
                     "  \\\\ A",
                     " \\\\\\\\\\  ",
                     " \\\\\\\\  ")

    def test_rstrip(self):
        expected_results = ("hello\\",
                            "te\\st\\\\",
                            "A\\ ",
                            "A\\ ",
                            "   A \\ \\ ",
                            "    \\ A \\ ",
                            "  \\\\ A",
                            " \\\\\\\\\\ ",
                            " \\\\\\\\")

        self.assertResultsEqual(
            unescaped_rstrip,
            {(test_string,): result
             for test_string, result in zip(self.test_strings2,
                                            expected_results)})

    def test_basic(self):
        expected_results = ("hello\\",
                            "te\\st\\\\",
                            "A\\ ",
                            "A\\ ",
                            "A \\ \\ ",
                            "\\ A \\ ",
                            "\\\\ A",
                            "\\\\\\\\\\ ",
                            "\\\\\\\\")

        self.assertResultsEqual(
            unescaped_strip,
            {(test_string,): result
             for test_string, result in zip(self.test_strings2,
                                            expected_results)})

    def test_no_whitespaced_strings(self):
        # When no leading or trailing whitespaces exist, nothing should happen.
        self.assertResultsEqual(
            unescaped_strip,
            {(test_string,): test_string
             for test_string in self.test_strings})


if __name__ == '__main__':
    unittest.main(verbosity=2)
