import click
from restcli import storage, http_client

@click.group("cli")
def cli():
    pass

@cli.command()
@click.argument('url')
@click.option('--count', '-c', default=1, help='Number of requests.')
def get(url, count):
    """Run HTTP get requests on given URL."""
    for c in range(count):
        response = http_client.get(url)
        click.echo(response.text)


@cli.command()
@click.argument('url')
@click.option('--count', '-c', default=1, help='Number of requests.')
def post(url, count):
    """Run HTTP post requests on given URL."""
    for c in range(count):
        response = http_client.post(url)
        click.echo(response.text)


@cli.command()
@click.argument('url')
@click.option('--count', '-c', default=1, help='Number of requests.')
def put(url, count):
    """Run HTTP put requests on given URL."""
    for c in range(count):
        response = http_client.put(url)
        click.echo(response.text)


@cli.command()
@click.argument('url')
@click.option('--count', '-c', default=1, help='Number of requests.')
def delete(url, count):
    """Run HTTP delete requests on given URL."""
    for c in range(count):
        response = http_client.delete(url)
        click.echo(response.text)


@cli.command()
@click.argument('url')
@click.option('--count', '-c', default=1, help='Number of requests.')
def head(url, count):
    """Run HTTP head requests on given URL."""
    for c in range(count):
        response = http_client.head(url)
        click.echo(response.text)


@cli.command()
@click.argument('url')
@click.option('--count', '-c', default=1, help='Number of requests.')
def options(url, count):
    """Run HTTP options requests on given URL."""
    for c in range(count):
        response = http_client.options(url)
        click.echo(response.text)


@cli.command()
def init():
    """Initialize application"""
    cluster_url = click.prompt('Inform URL to access cluster:')

if __name__ == '__main__':
    cli()
