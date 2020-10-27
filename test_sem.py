from semver_comparison import determinePrecedence
from sample_input import sample_input
import unittest


class TestPrecedence(unittest.TestCase):

    def test_isprecedent(self):
        for input in sample_input:
            self.assertEqual(determinePrecedence(input['v1'], input['v2']), input['expected_result'])


if __name__ == '__main__':
    unittest.main()