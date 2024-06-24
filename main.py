if __name__ == '__main__':
    x = int(input("Enter number : "))

    primes = []
    for i in range(2, x+1):
        is_p = True
        for j in range(2, i):
            if i % j == 0:
                is_p = False
        if is_p:
            primes.append(i)

    print(*primes)