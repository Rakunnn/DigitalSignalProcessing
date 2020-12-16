'''
Code: discrete time for DSP
'''

def time_function(n):
    x_n = 0
    if(n >= -4 and n <= 4):
        x_n = abs(n)
    else:
        x_n = 0
    return x_n 

def a(n):
    return time_function((n))

def b(n):
    return time_function((n-1))

def c(n):
    return time_function((n+1))

def d(n):
    return (1/3)*(a(n)+b(n)+c(n))

if __name__ == "__main__":
    for i in range(-4,5):
        print(f'b:x({i-1})={b(i)}')