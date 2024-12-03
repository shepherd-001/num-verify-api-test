import pytest
import subprocess

@pytest.mark.parametrize("users, spawn_rate", [
    (10, 2),
    (50, 5),
    (100, 10),
])
def test_stress_testing(users, spawn_rate):
    cmd = [
        "locust",
        "-f", "locustfile.py",
        "--headless",
        f"-u {users}",
        f"-r {spawn_rate}",
        "--run-time", "2m",
        # "--host", "http://your-api-host.com"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    # print(f'\nStress Test Result: {result.stdout}\n')
    # print(f'\nStress Test Result Error: {result.stderr}\n')

    assert result.returncode == 0, f'Locust test failed with code: {result.returncode}'
