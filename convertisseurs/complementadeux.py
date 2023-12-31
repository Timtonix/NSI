import re

import click


@click.command()
@click.option("--input-base", prompt="Input base", type=int)
@click.option("--output-base", prompt="Output base", type=int)
@click.option("--value", prompt="Value to convert", type=str)
def get_default_params(input_base, output_base, value):
    if input_base == 2 and output_base == 10:
        binary_to_decimal(value)


def binary_to_decimal(value: str):
    if not re.fullmatch("[01]+", value):
        raise ValueError(f"Unexpected values in {value}. We only accept 1 and 0 for this function")

    binary_list = [*value]
    binary_list = binary_list[::-1]


    base_ten = 0
    for i, number in enumerate(binary_list):


        number = int(number)

        if number == 1:
            base_ten += 2**i

    return base_ten


if __name__ == '__main__':
    get_default_params()