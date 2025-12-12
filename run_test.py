
import subprocess


def test_local_timezone_setting() -> None:
    completed_process = subprocess.run("date", capture_output=True)
    date_output = completed_process.stdout.decode()
    assert "EST" in date_output or "EDT" in date_output


def test_sudo() -> None:
    completed_process = subprocess.run(["sudo", "apt", "update"])
    completed_process.check_returncode()


def test_python() -> None:
    completed_process = subprocess.run("python3")
    assert completed_process.returncode == 0


def test_pip() -> None:
    completed_process = subprocess.run("pip3")
    assert completed_process.returncode == 0


def test_venv() -> None:
    completed_process = subprocess.run(["virtualenv", "--version"])
    assert completed_process.returncode == 0


def test_man_installed() -> None:
    completed_process = subprocess.run(["man", "-V"])
    assert completed_process.returncode == 0
