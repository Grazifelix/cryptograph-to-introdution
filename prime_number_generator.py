# 02/09/22
# Graziela Felix
import random


def prime_number_generator(prime_number_length):

    def prime_number_verification(number_init, number_end):
        boolean_var = True
        while boolean_var:
            count = 0
            prime_number = random.randint(number_init, number_end)
            # prime_number = 25
            end = prime_number+1
            if prime_number == 2 or prime_number % 2 != 0:
                for i in range(1, end):
                    if prime_number % i == 0:
                        count += 1
                        if count > 2:
                            # print(prime_number, " não é primo")
                            break
                else:
                    # print("É numero primo: ", prime_number)
                    #boolean_var = False
                    return prime_number

    # prime number range generator
    if prime_number_length > 1:
        p_num_r_init = "1"+("0"*(prime_number_length-1))
        p_num_r_end = "1"+("0"*prime_number_length)
        prime_number_range_init = int(p_num_r_init)
        prime_number_range_end = int(p_num_r_end)-1

        #print(prime_number_range_init)
        #print(prime_number_range_end)
        prime_number = prime_number_verification(prime_number_range_init, prime_number_range_end)
        return prime_number
    else:
        prime_number = prime_number_verification(1, 9)
        return prime_number


if __name__ == "__main__":
    key_number = int(input("Length of prime numbers keys: "))
    print(prime_number_generator(7))
