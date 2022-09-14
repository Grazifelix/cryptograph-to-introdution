from efficient_modular_exponentiation import efficient_modular_exponentiation
from large_prime_number_generator import large_prime_number_generator
import random
import math
from Crypto.Util import number

def rsa_cryptosystem(message_to_encode, prime_number_length):
    # choose two prime number (private keys) P and Q

    p = large_prime_number_generator(prime_number_length)
    q = large_prime_number_generator(prime_number_length)

    print('p: ', p)
    print('q: ', q)

    # calculate the product of the two keys
    n = p * q
    print('N: ', n)

    # euler's totient formula
    totient = (p - 1) * (q - 1)
    print("totient: ", totient)

    # select an aleatory co-prime number of N
    def co_prime_number(totient):
        while True:
            e_key = random.randint(1, totient)
            if math.gcd(n, e_key) == 1:
                print("E:", e_key)
                return e_key

    e_key = co_prime_number(totient)

    encrypt = []

    for uni_m in message_to_encode:
        result = efficient_modular_exponentiation(uni_m, e_key, n)
        encrypt.append(result)
    return encrypt



def main():
    message = input("Message: ")
    prime_number_length = int(input("Length of prime numbers keys: "))
    unicode_message = []
    for m in message:
        unicode_message.append(ord(m))
    print(unicode_message)
    print("Mensage: \n", " ".join(map(str, rsa_cryptosystem(unicode_message, prime_number_length))))

if __name__ == "__main__":
    main()
