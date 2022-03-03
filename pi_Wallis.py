def pi(n):
    chi = 2
    zn = 1
    pi = 2 * (2 / 1)
    for i in range(2, n):
        if i % 2 == 0:
            chi = chi
            zn = zn + 2
        if i % 2 != 0:
            chi = chi + 2
            zn = zn
        pi_i = chi / zn
        pi = pi * pi_i

        print(i, chi, zn, pi_i, pi)


if __name__ == "__main__":
    pi(1000000)
