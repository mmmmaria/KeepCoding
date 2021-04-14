# def retrocontador(e):
#     print("{},".format(e), end="")
#     if e > 0:
#         retrocontador(e-1)
# 
# retrocontador(10)

def sumatorio(n):
    print("{},".format(n), end="")
    if n > 0:
        return n + sumatorio(n-1)
    else:
        return 0
    
sumatorio(3)