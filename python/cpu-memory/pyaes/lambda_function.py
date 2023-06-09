from time import time
import random
import sys
import string
import pyaes


def generate(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))


def lambda_handler(length_of_message, num_of_iterations):
    message = generate(length_of_message)

    # 128-bit key (16 bytes)
    KEY = b'\xa1\xf6%\x8c\x87}_\xcd\x89dHE8\xbf\xc9,'

    start = time()
    for loops in range(num_of_iterations):
        aes = pyaes.AESModeOfOperationCTR(KEY)
        ciphertext = aes.encrypt(message)

        aes = pyaes.AESModeOfOperationCTR(KEY)
        plaintext = aes.decrypt(ciphertext)
        aes = None

    latency = time() - start
    return latency

if __name__ == "__main__":
    length_of_message = int(sys.argv[1])
    num_of_iterations = int(sys.argv[2])
    result = lambda_handler(length_of_message, num_of_iterations)
    print(result)
