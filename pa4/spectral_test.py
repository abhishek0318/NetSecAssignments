import matplotlib.pyplot as plt

from lcg import LCG

if __name__ == "__main__":
    #rnd_gen = LCG(m=31, a=3, c=0, x0=21)
    rnd_gen = LCG(m=31, a=13, c=0, x0=12)

    x = []
    y = []

    x_n = 31
    for i in range(1, 100):
        y.append(x_n)
        x_n = rnd_gen.next()
        x.append(x_n)
    
    print(x, y)

    plt.scatter(x, y)
    plt.xlabel('x(n)')
    plt.ylabel('x(n-1)')
    plt.title('Spectral Test')
    plt.show()
