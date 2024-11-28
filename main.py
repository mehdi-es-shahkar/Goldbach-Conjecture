# functions
def is_prime(n : int) -> bool:
    "This function takes an integer and returns True if it is prime and False otherwise."
    d = 2
    while d * d <= n:
        if n % d == 0 : return False
        d += 1
    return True

def goldbach(n):
    if n <= 0 : 
        print("pleae Enter positive integer !")
    if n % 2 == 1 :
          print(f"{n} is odd number . please Enter even number !")
          return 
    
    if n in [2, 4] : return True
    for i in range(3, n // 2 + 1):
        if is_prime(i) and is_prime(n - i) : return True
    return False

def write_in_file(add, filename, text) :
    with open(f"{add}/{filename}.txt", "w", encoding = "utf-8") as d:
        d.write(text)
    
def main():
    # add is directory address for save txt file in your pc for example "D:/Goldbach-Conjecture"
    add = "D:/Goldbach-Conjecture"
    filename = "Goldbach"
    filename_of_Contradiction = "Goldbach_Contradiction"
    number = 2
    step = 10000
    while True :
        if not goldbach(number) :
            text = f"A Contradiction Example for Goldenbach's Conjecture is --> {number} !!!"
            print(text)
            write_in_file(add, filename_of_Contradiction, text)
            return
        if number % step == 0:
            text = f"Goldbach's Conjecture is true up to  ---> {number} <--- !!!!!"
            print(text)
            write_in_file(add, filename, text)
        number += 2
        
if __name__ == "__main__" :
    main()
