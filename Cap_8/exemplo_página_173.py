# Configuração de funções com funções

def imprime_lista(L, fimpressão, fcondição):
    for e in L:
        if fcondição(e):
            fimpressão(e)
def imprime_elemento(e):
    print(f"Valor: {e}")
    
