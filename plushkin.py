import os
import click
import sys
import searcher as scr
import user_interface as ui
import cleaner as clr


@click.command(options_metavar='<path>',
               short_help='return duplicate files w/ their path')
@click.option('-d', '--delete',
              is_flag=True,
              help='Delete duplicates (Launch interactive cmd interface)',
              metavar='<flag>')
@click.argument('path')
def plushkin(path, delete):
    """ This script shows all the duplicates stored in your folders
        Optionally they can be deleted through interactive UI(use flag -d)
    """
    sys.excepthook = excepthook
    if os.path.isdir(path):
        search_results = scr.Searcher.search_clones(path)  # FM
        interface_reports = ui.UserInterface(search_results)
        interface_reports.show_search_report()
        if delete:
            for group_index in range(interface_reports.clone_groups_len):
                dup_group, save_index = interface_reports.show_cleaning_input(group_index)
                interface_reports.report(clr.Cleaner(dup_group, save_index)
                                         .clean_and_report())
            interface_reports.overall()
    else:
        raise DirectoryNotFoundException('Path not found')


class DirectoryNotFoundException(BaseException):
    """ Stub for the programmers(Will not be printed for user) """
    pass


def excepthook(type, value, traceback):
    """ Point how Exception messages should be treated"""
    print(f'Cannot be resolved - {value}')


if __name__ == '__main__':
    plushkin()
