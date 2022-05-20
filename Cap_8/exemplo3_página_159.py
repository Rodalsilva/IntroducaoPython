def épar(x):
    return x % 2 == 0
def par_ou_ímpar(x):
    if épar(x):
        return "par"
    else:
        return ímpar

print(par_ou_ímpar(4))
print(par_ou_ímpar(3))
