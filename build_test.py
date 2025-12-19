
import io
import json
import re

from pathlib import Path
from typing import Callable


def test_man_pages_exist() -> None:
    man_path = Path("/usr/share/man")
    man_files = list(man_path.glob("**/*.gz"))
    assert len(man_files) > 0


def snip_block(stream: io.TextIOBase, start: str, end: str) -> list[str]:
    result = []
    collecting = False
    while line := stream.readline():
        line = line.strip()
        if line == start:
            collecting = True
        elif line == end:
            collecting = False
        elif collecting:
            result.append(line)
    return result


def find_missing_items(
        required: list[str],
        existing: list[str],
        matches: Callable[[str, str], bool]
) -> list[str]:
    result = []
    required.sort()
    existing.sort()
    for item_required in required:
        found = False
        for item_existing in existing:
            if matches(item_existing, item_required):
                found = True
                break
        if not found:
            result.append(item_required)

    log_dict = {"required": required, "existing": existing, "result": result}
    print("find_missing_items", json.dumps(log_dict, indent=2))

    return result


def test_emacs_packages_exist() -> None:
    with open("install.el") as f:
        package_symbols = snip_block(
            f, ";; start-package-list", ";; end-package-list"
        )
    packages = [symbol.replace("'", "") for symbol in package_symbols]

    names_of_directories_in_emacs_d = [
        p.name
        for p in Path("/home/docker_usr/.emacs.d").glob("**")
        if p.is_dir()
    ]

    def directory_starts_with_package(directory: str, package: str) -> bool:
        return directory.startswith(package)

    missing_packages = find_missing_items(
        packages,
        names_of_directories_in_emacs_d,
        directory_starts_with_package
    )

    assert not missing_packages


def test_tree_sitter_grammars_exist() -> None:
    # a token is a char sequence without parentheses or spaces
    TOKEN_REGEXP = re.compile("[^'() ]+")

    def tree_sitter_grammar(line: str) -> str:
        # the first token in each item of treesit-language-source-alist
        # is the name of the grammar
        tokens = TOKEN_REGEXP.findall(line)
        return tokens[0]

    with open("install.el") as f:
        tree_sitter_lines = snip_block(
            f, ";; start-tree-sitter-list", ";; end-tree-sitter-list"
        )

    tree_sitter_grammars = [
        tree_sitter_grammar(line) for line in tree_sitter_lines
    ]

    names_of_libraries = [
        p.name
        for p in Path("/home/docker_usr/.emacs.d/tree-sitter").glob("**")
        if p.is_file()
    ]

    def library_name_contains_grammar(library_name: str, grammar: str) -> bool:
        return grammar in library_name

    missing_libraries = find_missing_items(
        tree_sitter_grammars,
        names_of_libraries,
        library_name_contains_grammar
    )

    assert not missing_libraries
