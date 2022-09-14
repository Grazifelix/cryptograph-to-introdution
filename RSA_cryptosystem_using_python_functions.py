import random
import math
from Crypto.Util import number

def rsa_cryptosystem(message_to_encode, prime_number_length):
    # choose two prime number (private keys) P and Q

    p = number.getPrime(prime_number_length*3)
    q = number.getPrime(prime_number_length*3)

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
            e_key = random.randint(2, totient)
            if math.gcd(n, e_key) == 1:
                print("E:", e_key)
                return e_key

    e_key = co_prime_number(totient)
    result = modular_exponentiation(message_to_encode, e_key, n)

    return result

def RSA_Decryption(mensage_to_decode, e_key, n_key):
    # calculating private key D
    i = 1
    tontient = int(input("t: "))
    while True:
        if e_key*i % tontient == 1:
            print("d vale: ", i)
            break
        i += 1

    result = modular_exponentiation(mensage_to_decode, i, n_key)
    print(result)

    return result


def modular_exponentiation(message_to_encode, e_key, n):
    encrypt = []

    for uni_m in message_to_encode:
        result = pow(int(uni_m), e_key, n)
        encrypt.append(result)
    return encrypt


def main():
    user_option = int(input("1-Encryption\n2-Decryption\n"))

    if user_option == 1:
        message = input("Message: ")
        print()
        prime_number_length = int(input("Length of prime numbers keys: "))
        unicode_message = []
        for m in message:
            unicode_message.append(ord(m))
        print(unicode_message)
        print(rsa_cryptosystem(unicode_message, prime_number_length))
    elif user_option == 2:
        # message = input("Message: ").split()
        # print(message)
        # public_key_e = int(input("Key E: "))
        # public_key_n = int(input("Key N: "))
        # mensage = RSA_Decryption(message, public_key_e, public_key_n)
        # decrypt_message = []
        # for m in mensage:
        #     decrypt_message.append(chr(m))
        # print(decrypt_message)
        print("not working yet")


if __name__ == "__main__":
    main()
