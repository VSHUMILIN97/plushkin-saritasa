import os
import click
import sys


@click.command()
@click.option('-d', '--delete',
              is_flag=True,
              help='Delete duplicates (Launch interactive cmd interface')
@click.argument('path')
def plushkin(path, delete):
    if os.path.isdir(path):
        print('Searcher look-up')
        if delete:
            for _ in range(3):
                print('Interface and cleaner')
    else:
        raise DirectoryNotFoundException('Path not found')


class DirectoryNotFoundException(BaseException):
    pass


def excepthook(type, value, traceback):
    print(value)


if __name__ == '__main__':
    sys.excepthook = excepthook
    plushkin()
