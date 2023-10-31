"""
CLI module for groups and commands
"""
import click


@click.group("inference-tools")
def cli() -> None:
    
    """ Inference related commands """
    return


@cli.command("search", help="inference search")
@click.option(
    "-s", 
    "--search", 
    "search", 
    type=click.STRING, 
    help="search option"
)
def search(search: str) -> None:
    
    click.echo("Searching for %s " % search)


@cli.command("run", help="inference run")
@click.option(
    "-r", 
    "--run", 
    "run", 
    type=click.BOOL, 
    help="run option"
)
def run(run: bool) -> None:
    
    click.echo("Running inference %s " % run)


if __name__ == "__main__":
    cli()
    