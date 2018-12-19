import click
from stop import get_xl_objects, get_axapta_data, apply_options, apply_values, save_reports

@click.group()
def cli():
    pass


@cli.command()
def stop():
    """Generate STOP report"""

    click.echo('\n-- GENERATE STOP REPORT -------------------------------------')

    click.echo('    creating workbook and getting data')
    workbook, worksheet = get_xl_objects()
    ax_data = get_axapta_data()

    click.echo('    applying worksheet options and cell values')
    apply_options(worksheet, ax_data)
    apply_values(worksheet, ax_data)

    click.echo('    saving workbook to drives')
    save_reports(workbook)

    click.echo('-- DONE -----------------------------------------------------\n')

@cli.command()
def mi():
    pass
