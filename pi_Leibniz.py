def pi(n):
    chi = 4
    zn = 1
    pi = 0
    for _ in range(1, n):
        pi_ = chi/zn
        chi = -1 * chi
        zn = zn + 2
        pi = pi + pi_
        print(_, pi)


if __name__ == "__main__":
    pi(1000000)
