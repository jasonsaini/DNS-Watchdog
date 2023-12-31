import socket
import time
import datetime

# Define four global IP addresses
ips = ["8.8.8.8", "1.1.1.1", "9.9.9.9", "208.67.222.222"]  # Example IPs

# Function to perform DNS resolution and count failures
def check_dns_resolution(ip):
    failure_count = 0
    googleIp, youtubeIp = "", ""
    for _ in range(50):
        try:
            googleIp = socket.gethostbyname("google.com")
        except socket.gaierror:
            failure_count += 1
            print(f"Failed to resolve google.com using IP {ip} at {datetime.datetime.now()}")
        try:
            youtubeIp = socket.gethostbyname("youtube.com")
        except socket.gaierror:
            failure_count += 1
            print(f"Failed to resolve youtube.com using IP {ip} at {datetime.datetime.now()}")
    return [failure_count, googleIp, youtubeIp]

# Run the script for approximately 10 minutes
start_time = time.time()
while time.time() - start_time < 600:  # 600 seconds = 10 minutes
    for ip in ips:
        results = check_dns_resolution(ip)
        if results[0] > 0:
            utc_timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{utc_timestamp} UTC] IP {ip} had {results[0]} DNS resolution failures in this iteration.")
        time.sleep(1)  # Adding a short delay to prevent excessive requests

print("Script completed. Total run time: approximately 10 minutes.")
