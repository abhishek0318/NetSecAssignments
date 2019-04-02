import math
import matplotlib.pyplot as plt

def eulers_totient_fn(num):
    count = 1
    for i in range(1, num):
        if math.gcd(i, num) == 1:
            count += 1
    return count

if __name__ == "__main__":
    plt.scatter(range(1, 1001), [eulers_totient_fn(i) for i in range(1, 1001)], s=2)
    plt.title('Euler\'s totient function')
    plt.xlabel('n')
    plt.ylabel('φ(n)')
    plt.show()
        
