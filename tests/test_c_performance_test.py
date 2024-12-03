import subprocess

def test_locust_performance():
    cmd = [
        "locust",
        "-f", "locustfile.py",
        "--headless",
        "-u", "10",    # Number of users
        "-r", "2",     # Spawn rate
        "--run-time", "1m",  # Duration of the test
        # "--host", "http://your-api-host.com"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    # print(f'\nPerformance Test Result: {result.stdout}\n')
    # print(f'\nPerformance Test Result Error: {result.stderr}\n')

    assert result.returncode == 0, f'Locust test failed with code: {result.returncode}'
