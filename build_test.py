
from pathlib import Path


def test_man_pages_exist() -> None:
    man_path = Path("/usr/share/man")
    man_files = list(man_path.glob("**/*.gz"))
    assert len(man_files) > 0
