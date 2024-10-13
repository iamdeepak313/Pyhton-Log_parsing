import re
import csv
import collections

def log_file_reader(filename):
    # Get all IP addresses from the log file
    ip_list = []
    with open(filename) as f:
        for row in f:
            regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            ip_list.extend(re.findall(regex, row))
    return ip_list

# Get total count of IPs
def count_ip(ip_list):
    return collections.Counter(ip_list)

def write_to_csv(counter):
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Count']
        writer.writerow(header)
        for item, count in counter.items():
            writer.writerow((item, count))

if __name__ == "__main__":
    ip_list = log_file_reader('/home/deepak/Desktop/log')  # Specify your log filename here
    ip_counter = count_ip(ip_list)
    write_to_csv(ip_counter)
