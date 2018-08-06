import unittest
from cleaner import Cleaner


class CleanerTest(unittest.TestCase):

    def test_that_always_success(self):
        """ Always Success! """
        self.assertTrue(True)

    def test_cleaner_instance_get_attribute_fails(self):
        """ Checks that it is not possible to get attribute"""
        cc = Cleaner(['/path/to/file', '/another/one'], 1)
        with self.assertRaises(AttributeError):
            print(cc.__files_removed)

    def test_cleaner_erase_given_data(self):
        """ Checks if it is possible to delete a file

        Notes:
             58 is hard-coded. DO NOT CHANGE
        """
        file = open('plushkin1', 'w+')
        file.close()
        file = open('plushkin2', 'w+')
        file.close()
        cc = Cleaner(['plushkin1', 'plushkin2'], 0)
        self.assertEqual(cc.clean_and_report(), ([], 1, 58, 0))

    def test_cleaner_return_mistakes_correctly(self):
        """ Checks if mistakes returned correctly """
        notcc = Cleaner(['pp', 'tt'], 1)
        self.assertEqual(notcc.clean_and_report(),
                         (['pp is not a file!'], 0, 0, 1))

    def test_app_not_crash_on_invalid_data_type(self):
        """ Checks if app will crash on invalid data type """
        cc = Cleaner(1, 2)
        self.assertEqual(cc.clean_and_report(), ([], 0, 0, 0))
