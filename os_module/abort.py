import subprocess

result = subprocess.run(["python", "os1.py"])
print("Exit code:", result.returncode)