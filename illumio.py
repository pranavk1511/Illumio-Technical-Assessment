import csv
import sys
from collections import defaultdict

PROTOCOL_NAME_TO_NUMBER = {
    'tcp': 6,
    'udp': 17,
    'icmp': 1
}

PROTOCOL_NUMBER_TO_NAME = {v: k for k, v in PROTOCOL_NAME_TO_NUMBER.items()}

def read_lookup_table(lookup_file_path):
    lookup_table = {}
    try:
        with open(lookup_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dstport = int(row['dstport'])
                protocol_name = row['protocol'].lower()
                tag = row['tag']
                protocol_number = PROTOCOL_NAME_TO_NUMBER.get(protocol_name)

                if protocol_number is None:
                    continue  

                key = (dstport, protocol_number)
                lookup_table[key] = tag
    except Exception as e:
        print(f"Error reading lookup table: {e}")
        sys.exit(1)
    return lookup_table

def process_flow_logs(flow_log_file_path, lookup_table):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    try:
        with open(flow_log_file_path, 'r') as logfile:
            for line in logfile:
                if not line.strip():
                    continue  
                fields = line.strip().split()
                if len(fields) < 14:
                    continue  

                dstport = int(fields[6])  
                protocol_number = int(fields[7])

                protocol_name = PROTOCOL_NUMBER_TO_NAME.get(protocol_number, str(protocol_number))

                
                port_protocol_key = (dstport, protocol_name)
                port_protocol_counts[port_protocol_key] += 1

                
                lookup_key = (dstport, protocol_number)
                tag = lookup_table.get(lookup_key, 'Untagged')
                tag_counts[tag] += 1

    except Exception as e:
        print(f"Error processing flow logs: {e}")
        sys.exit(1)

    return tag_counts, port_protocol_counts

def output_results(tag_counts, port_protocol_counts):
    print("Tag Counts:\n")
    print("Tag,Count")
    for tag, count in tag_counts.items():
        print(f"{tag},{count}")

    print("\nPort/Protocol Combination Counts:\n")
    print("Port,Protocol,Count")
    for (port, protocol), count in port_protocol_counts.items():
        print(f"{port},{protocol},{count}")

def main():
    if len(sys.argv) != 3:
        print("Incorrect number of arguments. Usage: python illumio.py <flow_log_file_path> <lookup_file_path>")
        sys.exit(1)

    flow_log_file_path = sys.argv[1]
    lookup_file_path = sys.argv[2]
    

    lookup_table = read_lookup_table(lookup_file_path)
    tag_counts, port_protocol_counts = process_flow_logs(flow_log_file_path, lookup_table)
    output_results(tag_counts, port_protocol_counts)

if __name__ == "__main__":
    main()
