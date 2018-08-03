import unittest
from unittest import mock


class MyTestCase(unittest.TestCase):
    @mock.patch("Searcher.open")
    def test_something(self, mock_open):
        pass


if __name__ == '__main__':
    unittest.main()
