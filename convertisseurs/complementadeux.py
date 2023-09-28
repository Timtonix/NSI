import click


@click.command()
@click.option("--input-base", prompt="Input base", type=int)
@click.option("--output-base", prompt="Output base", type=int)
@click.option("--value", prompt="Value to convert", type=int)
def get_default_params(input_base, output_base, value):
    click.echo(input_base)
    click.echo(output_base)
    click.echo(value)


if __name__ == '__main__':
    get_default_params()