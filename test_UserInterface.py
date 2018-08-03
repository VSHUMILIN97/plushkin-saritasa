import unittest
from UserInterface import UserInterface


class TestUserInterface(unittest.TestCase):

    class SampleReport:

        def __init__(self):
            self.clone_groups = {
                0: [
                    '/home/alexey/Downloads/masteringdjangocore-sample.pdf',
                    '/home/alexey/Downloads/paris.ps',
                    '/home/alexey/Downloads/IMG_1665.JPG'
                ],
                1: [
                    '/home/alexey/Downloads/Fluent_Python.pdf',
                    '/home/alexey/Downloads/Photos1/IMG_1670.JPG',
                    '/home/alexey/Downloads/IMG_1664.JPG'
                ]
            }
            self.unavailable_files = {'can not read anything!!!', 'what to do?'}
            self.scanned_files_num = 43
            self.scanned_folders_num = 12
            self.duplications_num = 33
            self.name_scanned_folder = '/dd/qwd/qwdw'

    sample_report = SampleReport()

    ui = UserInterface(sample_report)

    def test_general_information(self):

        self.ui.show_cleaning_input(0)

    def test_exceptions(self):

        self.ui.exceptions_information()

    def test_show_search_report(self):

        self.ui.show_search_report()

    def test_show_cleaning_input(self):

        # we suppose that a user entered 1
        self.assertEqual(
            self.ui.show_cleaning_input(0),
            (
                [
                    '/home/alexey/Downloads/masteringdjangocore-sample.pdf',
                    '/home/alexey/Downloads/paris.ps',
                    '/home/alexey/Downloads/IMG_1665.JPG'
                ],
                1
            )
        )

    def test_report(self):

        cl_report1 = (['mistake1', 'mistake2'], 1, 2, 3)
        cl_report2 = (['mistake4', 'mistake5'], 6, 8, 9)

        self.ui.report(cl_report1)
        self.ui.report(cl_report2)

    def test_overall(self):

        self.ui.overall()


if __name__ == '__main__':
    unittest.main()
