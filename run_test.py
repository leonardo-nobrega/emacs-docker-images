
import subprocess


def test_local_timezone_setting() -> None:
    completed_process = subprocess.run("date", capture_output=True)
    date_output = completed_process.stdout.decode()
    assert "EST" in date_output or "EDT" in date_output
