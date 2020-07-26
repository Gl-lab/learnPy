import click

from language_sort.sorter.api.api import API
from language_sort.sorter.local_files.local_files import LocalFiles


@click.group()
def cli():
    pass


@cli.command()
@click.argument("text", nargs=-1)
@click.option('-f', "--file", type=click.File('r'))
def get_language(text, file):
    text = file.read() if file is not None else " ".join(text)
    api = API()
    api.pull_languages(text)
    language = api.get_language(text)
    click.echo(language)


@cli.command()
@click.argument('src', type=click.Path(exists=True, dir_okay=True))
@click.argument('dst', type=click.Path(dir_okay=True))
def sort_files(src, dst):
    lf = LocalFiles(src, dst)
    lf.prepare_paths()
    lf.move_files()


if __name__ == '__main__':
    cli()
