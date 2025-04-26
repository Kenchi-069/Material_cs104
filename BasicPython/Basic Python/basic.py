def givePrimeList(n):
    ans = []
    for i in range(2,n*n):
        isPrime = True
        for d in range(2,i-1):
            if(i%d == 0):
                isPrime = False
                break
        if(isPrime):  
            ans.append(i)
        if(len(ans) >= n):
            break

    return ans

x = input("Hello mf give number")

my_Primes = givePrimeList(int(x))

for i in range(int(x)):
    if(my_Primes[i]-my_Primes[i-1] == 2): 
        print(my_Primes[i], my_Primes[i])
    else:
        print(my_Primes[i])