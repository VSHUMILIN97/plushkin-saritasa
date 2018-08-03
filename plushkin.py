import os
import click
import sys


@click.command(options_metavar='<path>',
               short_help='return duplicate files w/ their path')
@click.option('-d', '--delete',
              is_flag=True,
              help='Delete duplicates (Launch interactive cmd interface)',
              metavar='<flag>')
@click.argument('path')
def plushkin(path, delete):
    """ This function fetch all the duplicates from your directory path
        Optionally they can be deleted through interactive UI(use flag -d)
    """
    sys.excepthook = excepthook
    if os.path.isdir(path):
        print('Searcher look-up')
        if delete:
            for _ in range(3):
                print('Interface and cleaner')
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
