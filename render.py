
import jinja2 as j

from argparse import ArgumentParser
from os.path import exists
from typing import Any


def render(arguments: dict[str, Any]) -> None:
    env = j.Environment(
        loader=j.FileSystemLoader("."),
        lstrip_blocks=True,
        trim_blocks=True
    )
    template = env.get_template("Dockerfile.template")
    rendered = template.render(**arguments)
    with open("Dockerfile", "w") as f:
        f.write(rendered)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--force", action="store_true")
    parser.add_argument("-t", "--test", action="store_true")
    args = parser.parse_args()
    args_dict = {"test": args.test}
    if args.force:
        render(args_dict)
    elif exists("Dockerfile"):
        print("Overwrite the Dockerfile? [N/y]")
        overwrite = input()
        if overwrite.strip().lower() == "y":
            render(args_dict)
