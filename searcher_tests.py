import unittest
from unittest import mock
from Search.Searcher import Searcher
import os


class MyTestCase(unittest.TestCase):
    @mock.patch("Searcher.Searcher.open")
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
