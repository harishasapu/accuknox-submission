from collections import Counter

LOG_FILE = "sample_access.log"  # Path to your web server log file

# Counters to track stats
status_count = Counter()
page_count = Counter()
ip_count = Counter()

# Read the log file
with open(LOG_FILE, 'r') as file:
    for line in file:
        parts = line.split()
        if len(parts) < 9:
            continue  # Skip malformed lines

        ip = parts[0]
        status = parts[8]
        page = parts[6]

        status_count[status] += 1
        page_count[page] += 1
        ip_count[ip] += 1

# Print summary
print("=== Web Server Log Summary ===\n")
print(f"Total 404 errors: {status_count.get('404', 0)}\n")

print("Top 10 Requested Pages:")
for page, count in page_count.most_common(10):
    print(f"{page}: {count} requests")
print()

print("Top 10 IP Addresses:")
for ip, count in ip_count.most_common(10):
    print(f"{ip}: {count} requests")
