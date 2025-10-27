import subprocess
from datetime import datetime

# === Configuration ===
SOURCE_DIR = "/root"             # Local folder to back up
REMOTE_USER = "root"     # Remote server username
REMOTE_HOST = "13.221.81.254"  # Remote server IP or hostname
REMOTE_PATH = "/opt"             # Remote base folder
LOG_FILE = "backup_report.log"   # Local log file

# === Generate timestamps ===
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
remote_backup_path = f"{REMOTE_PATH}/{timestamp}"  

# === Backup process ===
try:
    # 1. Create remote backup folder
    subprocess.run(
        ["ssh", f"{REMOTE_USER}@{REMOTE_HOST}", f"mkdir -p {remote_backup_path}"],
        check=True
    )

    # 2. Copy local files to remote
    subprocess.run(
        ["scp", "-r", SOURCE_DIR, f"{REMOTE_USER}@{REMOTE_HOST}:{remote_backup_path}"],
        check=True
    )

    message = f"[{time_now}] Backup SUCCESS: {SOURCE_DIR} -> {REMOTE_HOST}:{remote_backup_path}"
except subprocess.CalledProcessError as e:
    message = f"[{time_now}] Backup FAILED: {e}"
except Exception as e:
    message = f"[{time_now}] Backup FAILED: {e}"

# 3. Write to log
with open(LOG_FILE, "a") as log_file:
    log_file.write(message + "\n")

# 4. Print result
print(message)

