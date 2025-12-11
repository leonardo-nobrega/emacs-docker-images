
import jinja2 as j

from argparse import ArgumentParser
from os.path import exists
from typing import Any

LANGUAGES = ["py"]
TEMPLATE_FILES = ["Dockerfile", "bashrc"]


def render_file(
        env: j.Environment, file_name: str, arguments: dict[str, Any]
) -> None:
    template = env.get_template(file_name + ".template")
    rendered = template.render(**arguments)
    with open(file_name, "w") as f:
        f.write(rendered)


def render(arguments: dict[str, Any]) -> None:
    env = j.Environment(
        loader=j.FileSystemLoader("."),
        lstrip_blocks=True,
        trim_blocks=True
    )
    for file_name in TEMPLATE_FILES:
        render_file(env, file_name, arguments)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--force", action="store_true")
    parser.add_argument("-t", "--test", action="store_true")
    parser.add_argument(
        "-l", "--lang",
        nargs="*", action="extend",
        choices=LANGUAGES
    )
    args = parser.parse_args()
    args_dict = {"test": args.test}

    # add a "lang_" attribute with value True for every lang argument
    selected_languages = args.lang or []
    if args.test:
        # include all languages if we are testing
        selected_languages = LANGUAGES
    for lang in selected_languages:
        args_dict["lang_" + lang] = True

    if args.force:
        render(args_dict)
    elif exists("Dockerfile"):
        print("Overwrite the Dockerfile? [N/y]")
        overwrite = input()
        if overwrite.strip().lower() == "y":
            render(args_dict)
