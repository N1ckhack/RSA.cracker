import pyfiglet
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes
import sys
import time
print(pyfiglet.figlet_format("RSA.CRACKER", font = "slant", width = 100))

def brute_force(ciphertext, public_key):
    n = public_key.n

    print("Bruteforcing in progress:")
    start_time = time.time()

    for i in range(2, n):
        if i % 1000 == 0:
            progress_percentage = (i / n) * 100
            sys.stdout.write("\rProgress: {:.2f}%".format(progress_percentage))
            sys.stdout.flush()

        if pow(i, public_key.e, n) == ciphertext:
            sys.stdout.write("\n")
            elapsed_time = time.time() - start_time
            print(f"Time taken for brute force: {elapsed_time:.2f} seconds")
            return long_to_bytes(i)

    sys.stdout.write("\n")
    elapsed_time = time.time() - start_time
    print(f"Time taken for brute force: {elapsed_time:.2f} seconds")
    return None

def rsa_crack(ciphertext, public_key):
    # Брутфорс
    recovered_message = brute_force(ciphertext, public_key)

    if recovered_message:
        print(f"Recovered message: {recovered_message}")
    else:
        print("Bruteforce failed.")

if __name__ == "__main__":
    rsa_crack(ciphertext = 0x993fb11, public_key = RSA.construct((0x112d25df, 0x578ba8f))) # (n, e)