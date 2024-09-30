import random
import time

def generate_flow_log_entry():
    version = '2'
    account_id = '123456789012'
    eni_id = 'eni-0a1b2c3d'
    srcaddr = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    dstaddr = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    srcport = str(random.randint(1, 65535))
    dstport = str(random.randint(1, 65535))
    protocol = str(random.choice([6, 17, 1]))  # TCP, UDP, ICMP
    packets = str(random.randint(1, 10000))
    bytes_sent = str(random.randint(1, 1000000))
    start_time = str(int(time.time()) - random.randint(0, 10000))
    end_time = str(int(time.time()))
    action = random.choice(['ACCEPT', 'REJECT'])
    log_status = 'OK'
    log_entry = f"{version} {account_id} {eni_id} {srcaddr} {dstaddr} {srcport} {dstport} {protocol} {packets} {bytes_sent} {start_time} {end_time} {action} {log_status}\n"
    return log_entry

def generate_flow_log_file(filename, target_size_mb):
    with open(filename, 'w') as file:
        size_in_bytes = target_size_mb * 1024 * 1024
        while file.tell() < size_in_bytes:
            log_entry = generate_flow_log_entry()
            file.write(log_entry)

generate_flow_log_file('./data/flow_logs_gen.txt', 10)
