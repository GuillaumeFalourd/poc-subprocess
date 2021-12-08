import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-c", "raise ValueError('oops')"], capture_output=True, text=True
)
print("stdout:", result.stdout)
print("stderr:", result.stderr)