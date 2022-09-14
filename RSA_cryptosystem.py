from efficient_modular_exponentiation import efficient_modular_exponentiation
from large_prime_number_generator import large_prime_number_generator
import random
import math


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

    # calculating private key D
    # def find_d(e, totient):
    #     i = 1
    #     bb = True
    #     for i in range(0, totient-1):
    #         if (e * i) % totient == 1:
    #             print("d:", i)
    #             bb = False
    #             return i
    #         i += 1
    #     print("Não encontrado")
    #
    #     # while bb:
    #     #     if (e * i) % totient == 1:
    #     #         print("d:", i)
    #     #         bb = False
    #     #         return i
    #     #     i += 1

    e_key = co_prime_number(totient)
    encrypt = []

    for uni_m in message_to_encode:
        result = efficient_modular_exponentiation(uni_m, e_key, n)
        encrypt.append(result)
    return encrypt

    # d = find_d(e, totient)
    # print(d)


def main():
    message = input("Message: ")
    prime_number_length = int(input("Length of prime numbers keys: "))
    unicode_message = []
    for m in message:
        unicode_message.append(ord(m))
    print(unicode_message)
    print(rsa_cryptosystem(unicode_message, prime_number_length))


if __name__ == "__main__":
    main()
