from time import time
import gzip
import os
import sys


def lambda_handler(file_size):
    file_write_path = 'tmp/file'

    start = time()
    with open(file_write_path, 'wb') as f:
        f.write(os.urandom(file_size * 1024 * 1024))
    disk_latency = time() - start

    with open(file_write_path, 'rb') as f:
        start = time()
        with gzip.open('tmp/result.gz', 'wb') as gz:
            gz.writelines(f)
        compress_latency = time() - start

    print(compress_latency)

    return {'disk_write': disk_latency, "compress": compress_latency}

if __name__ == "__main__":
    file_size = int(sys.argv[1])
    result = lambda_handler(file_size)
    print(result)
