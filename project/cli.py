import click
import datetime
from api import API
from local_files import LocalFiles


@click.group()
def cli():
    pass


@cli.command()
@click.option('--date', type=click.DateTime(formats=["%Y-%m-%d"]),
              default=str(datetime.datetime.today().strftime("%Y-%m-%d")))
def get_statistics(date):
    api = API()
    print(api.get_cases_by_date(date))

if __name__ == '__main__':
    cli()
