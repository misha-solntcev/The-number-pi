from math import sqrt


def pi(n):
    chi = 1
    z = 3
    pi = 1
    for i in range(1, n):
        chi = -1 * chi
        zn = z * 3**i
        pi_ = chi/zn
        pi = pi + pi_
        z = z + 2
        print(i, pi_, pi*sqrt(12))
        
    
        

if __name__ == "__main__":
    pi(35)
