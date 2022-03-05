# Вычисление числа пи по формуле Simon Plouff.
def pi(n):
    pi = 0
    for k in range(n):
        pi_k = 1 / 16**k * (4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
        pi = pi_k + pi
        print(k, pi_k, pi)


if __name__ == "__main__":
    pi(11)
