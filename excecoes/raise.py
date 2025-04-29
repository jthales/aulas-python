calculo = 0

def media(lista: list=[0]) -> float:
    calculo = sum(lista) / len(lista)

    if len(lista) > 4:
        raise ValueError("A lista não pode possuir mais de 4 notas.")
    

    if len(lista) < 4:
        raise ValueError("A lista não pode possuir menos de 4 notas.")
        
    return calculo

try:
    notas = [6, 7, 8, 10]
    resultado = media(notas)

except TypeError:
    print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")
    
except ValueError as e:
    print(e)

else:
    print(resultado)

finally:
    print("A consulta foi encerrada!")