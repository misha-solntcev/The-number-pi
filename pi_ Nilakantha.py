def pi(n):
    chi = -4
    z = 2
    pi = 3
    for _ in range(1, n):
        chi = -1 * chi
        zn = z*(z+1)*(z+2)
        pi_ = chi/zn
        pi = pi + pi_
        z = z + 2
        print(_, pi)


if __name__ == "__main__":
    pi(132000)
