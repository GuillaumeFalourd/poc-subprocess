import subprocess
import sys

result = subprocess.run([sys.executable, "-c", "raise ValueError('oops')"])
result.check_returncode()