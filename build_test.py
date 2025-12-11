
import io

from pathlib import Path


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

    missing_packages = []
    for package in packages:
        found = False
        for name in names_of_directories_in_emacs_d:
            if name.startswith(package):
                found = True
                break
        if not found:
            missing_packages.append(package)

    assert not missing_packages
