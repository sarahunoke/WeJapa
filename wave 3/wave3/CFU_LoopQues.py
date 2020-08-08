#Coding Quiz: Check for Prime Numbers

check_prime = [26, 39, 51, 53, 57, 79, 85]

#function that gets the factors of a number
def get_factor(number):
    factors = [str(i) for i in range(2, number-1) if (number % i) == 0]
    return factors

#function that prints non-prime numbers and factors
def not_a_prime(number):
    
      factors = get_factor(number)
      if factors == []:
          pass
      else:
          print(f"{number} is not a prime number, because it is a factor of {factors[0]}")


for number in check_prime:
    not_a_prime(number)