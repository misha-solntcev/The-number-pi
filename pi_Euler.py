from math import sqrt


def pi(n):
    chi = 1
    z = 1
    pi = 0
    for i in range(n):
        zn = z * z
        pi_ = chi/zn
        pi = pi + pi_
        print(i, z, chi, zn, pi_, pi)
        z = z + 1
        print(sqrt(pi*6))


if __name__ == "__main__":
    pi(1000)
