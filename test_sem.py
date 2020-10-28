from semver_comparison import determinePrecedence, get_highest_precedence
from sample_input import sample_input, version_list
import unittest


class TestPrecedence(unittest.TestCase):

    def test_isprecedent(self):
        for input in sample_input:
            self.assertEqual(determinePrecedence(input['v1'], input['v2']), input['expected_result'])

    def test_highest_precedence(self):
        self.assertEqual(get_highest_precedence(version_list['array_list']), version_list['output'])

if __name__ == '__main__':
    unittest.main()
