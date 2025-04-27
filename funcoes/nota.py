media_nota = 0
situacao = ""

def media(lista):
    soma = sum(lista) / len(lista)
    return soma.__round__(2)

def boletim(lista):
    media_nota = media(lista)
    
    if media_nota >= 7:
        situacao = "Aprovado"
    elif media_nota >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    return media_nota, situacao

media_nota, situacao = boletim([10, 8, 7])
print(f"Média: {media_nota} - Situação: {situacao}")