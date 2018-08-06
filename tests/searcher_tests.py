import unittest
from unittest import mock
from searcher import Searcher


class MyTestCase(unittest.TestCase):

    @mock.patch("builtins.open")
    @mock.patch('Searcher.os.path.getsize')
    @mock.patch('Searcher.filecmp.cmp')
    @mock.patch("Searcher.glob.glob")
    @mock.patch("Searcher.os.walk")
    def test_gather_equals_files_in_one_group(self,
                                              mock_os_walk,
                                              mock_glob,
                                              mock_cmp,
                                              mock_getsize,
                                              mock_open):
        mock_os_walk.return_value = ['some_dir1', 'some_dir2']
        mock_getsize.return_value = 1024
        mock_glob.return_value = ['some_file_1', 'some_file_2', 'some_file_3']
        mock_cmp.return_value = True
        mock_open.return_value = mock.MagicMock(side_effect=None)
        result = Searcher.search_clones('path')
        self.assertDictEqual(result.clone_groups, {0: ['some_file_1',
                                                       'some_file_2',
                                                       'some_file_3']})
        self.assertSetEqual(result.unavailable_files, set())
        self.assertEqual(result.scanned_files_num, 3)
        self.assertEqual(result.name_scanned_folder, 'path')
        self.assertEqual(result.scanned_folders_num, 2)

    @mock.patch("builtins.open")
    @mock.patch('Searcher.os.path.getsize')
    @mock.patch('Searcher.filecmp.cmp')
    @mock.patch("Searcher.glob.glob")
    @mock.patch("Searcher.os.walk")
    def test_empty_group_clones_if_size_zero(self,
                                             mock_os_walk,
                                             mock_glob,
                                             mock_cmp,
                                             mock_getsize,
                                             mock_open):
        mock_os_walk.return_value = ['some_dir1', 'some_dir2']
        mock_getsize.return_value = 0
        mock_glob.return_value = ['some_file_1', 'some_file_2', 'some_file_3']
        mock_cmp.return_value = True
        mock_open.return_value = mock.MagicMock(side_effect=None)
        result = Searcher.search_clones('path')
        self.assertDictEqual(result.clone_groups, {})
        self.assertSetEqual(result.unavailable_files, set())
        self.assertEqual(result.scanned_files_num, 3)
        self.assertEqual(result.name_scanned_folder, 'path')
        self.assertEqual(result.scanned_folders_num, 2)

    @mock.patch("builtins.open")
    @mock.patch('Searcher.os.path.getsize')
    @mock.patch('Searcher.filecmp.cmp')
    @mock.patch("Searcher.glob.glob")
    @mock.patch("Searcher.os.walk")
    def test_empty_group_clones_if_raises_exception(self,
                                                    mock_os_walk,
                                                    mock_glob,
                                                    mock_cmp,
                                                    mock_getsize,
                                                    mock_open):
        mock_os_walk.return_value = ['some_dir1', 'some_dir2']
        mock_getsize.return_value = 1024
        mock_glob.return_value = ['some_file_1', 'some_file_2', 'some_file_3']
        mock_open.side_effect = mock.MagicMock(side_effect=PermissionError)
        mock_cmp.return_value = PermissionError("Denied")
        result = Searcher.search_clones('path')
        self.assertDictEqual(result.clone_groups, {})
        self.assertSetEqual(result.unavailable_files, {'some_file_1', 'some_file_2', 'some_file_3'})
        self.assertEqual(result.scanned_files_num, 3)
        self.assertEqual(result.name_scanned_folder, 'path')
        self.assertEqual(result.scanned_folders_num, 2)

    @mock.patch("builtins.open")
    @mock.patch('Searcher.os.path.getsize')
    @mock.patch('Searcher.filecmp.cmp')
    @mock.patch("Searcher.glob.glob")
    @mock.patch("Searcher.os.walk")
    def test_empty_group_if_no_equal(self,
                                     mock_os_walk,
                                     mock_glob,
                                     mock_cmp,
                                     mock_getsize,
                                     mock_open):
        mock_os_walk.return_value = ['some_dir1', 'some_dir2']
        mock_getsize.return_value = 1024
        mock_glob.return_value = ['some_file_1', 'some_file_2', 'some_file_3']
        mock_open.return_value = mock.MagicMock(side_effect=None)
        mock_cmp.return_value = False
        result = Searcher.search_clones('path')
        self.assertDictEqual(result.clone_groups, {})
        self.assertSetEqual(result.unavailable_files, set())
        self.assertEqual(result.scanned_files_num, 3)
        self.assertEqual(result.name_scanned_folder, 'path')
        self.assertEqual(result.scanned_folders_num, 2)


if __name__ == '__main__':
    unittest.main()