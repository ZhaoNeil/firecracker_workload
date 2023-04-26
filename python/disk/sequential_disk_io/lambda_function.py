from time import time
import subprocess
import os
import sys

def lambda_handler(file_size, byte_size):
    file_write_path = 'tmp/file'
    
    start = time()
    with open(file_write_path, 'wb', buffering=byte_size) as f:
        f.write(os.urandom(file_size * 1024 * 1024))
        f.flush()
        os.fsync(f.fileno())
    disk_write_latency = time() - start
    disk_write_bandwidth = file_size / disk_write_latency 

    output = subprocess.check_output(['ls', '-alh', 'tmp/'])
    print(output)
    
    # start = time()
    # with open(file_write_path, 'rb', buffering=byte_size) as f:
    #     byte = f.read(byte_size)
    #     while byte != "":
    #         byte = f.read(byte_size)
    # disk_read_latency = time() - start
    # disk_read_bandwidth = file_size / disk_read_latency 

    rm = subprocess.Popen(['rm', '-rf', file_write_path])
    rm.communicate()
    
    return {
        'disk_write_bandwidth':disk_write_bandwidth, 
        'disk_write_latency':disk_write_latency,
        # 'disk_read_bandwidth':disk_read_bandwidth, 
        # 'disk_read_latency':disk_read_latency
    }

if __name__ == "__main__":
    file_size = int(sys.argv[1])
    byte_size = int(sys.argv[2])
    result = lambda_handler(file_size, byte_size)
    print(result)
