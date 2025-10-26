import psutil
import logging

CPU_THRESHOLD = 80
MEM_THRESHOLD = 65
DISK_THRESHOLD = 90
PROCESS_THRESHOLD = 300
LOG_FILE = "system_health.log"
 
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
 
def alert(message):
    print(message)
    logging.warning(message)
 
cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
process_count = len(psutil.pids())

print("-------System Health Report------")
print(f"CPU: {cpu}%")
print(f"Memory: {mem}%")
print(f"Disk: {disk}%")
print(f"Running Processes: {process_count}")

 
if cpu > CPU_THRESHOLD:
    alert(f"High CPU usage: {cpu}%")
if mem > MEM_THRESHOLD:
    alert(f"High Memory usage: {mem}%")
if disk > DISK_THRESHOLD:
    alert(f"High Disk usage: {disk}%")
if process_count > PROCESS_THRESHOLD:
    alert(f"High number of running processes: {process_count}")
