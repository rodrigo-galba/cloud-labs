import click

@click.group("cli")
def cli():
    pass

@cli.command()
@click.argument('name')
@click.option('--count', default=1, help='Number of greetings.')
def hello(count, name):
    """Say Hello for given NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    cli()
