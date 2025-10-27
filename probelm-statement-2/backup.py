import subprocess
from datetime import datetime

SOURCE_DIR = "/path/to/your/folder"
REMOTE_USER = "username"
REMOTE_HOST = "remote.server.com"
REMOTE_PATH = "/remote/backup/folder"
LOG_FILE = "backup_report.log"

time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    subprocess.run(f"ssh {REMOTE_USER}@{REMOTE_HOST} 'mkdir -p {REMOTE_PATH}'", shell=True, check=True)
    subprocess.run(f"scp -r {SOURCE_DIR} {REMOTE_USER}@{REMOTE_HOST}:{REMOTE_PATH}", shell=True, check=True)
    message = f"[{time_now}] Backup SUCCESS: {SOURCE_DIR} -> {REMOTE_HOST}:{REMOTE_PATH}"
except Exception as e:
    message = f"[{time_now}] Backup FAILED: {e}"

with open(LOG_FILE, "a") as log_file:
    log_file.write(message + "\n")

print(message)
