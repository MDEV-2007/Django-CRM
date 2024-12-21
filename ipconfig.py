import subprocess

def run_ipconfig():
    result = subprocess.run(["ipconfig"], capture_output=True, text=True)
    print(result.stdout)

run_ipconfig()