def reverse(array):
    return array[::-1]

array = [1, 2, 3]
print(f"O reverso do array é: {reverse(array)}");


def find_max(array):
    maior = array[0]
    for i in range(1, len(array)):
        if array[i] > maior:
            maior = array[i]
    return maior

arr = [34, 25, 89, 92]
print(find_max(arr));

def find_min(array):
    minimo = array[0]
    for num in array:
        if num < minimo:
            minimo = num
        return minimo
    
array = [10, 20, 30, 40, 50, 60, 70, 80]
print(find_min(array));

def find_sum(array):
    soma = 0
    for num in array:
        soma += num # (soma = soma + num)
    return soma

arr = [25, 20, 10]
print(find_sum(arr));

def palindromo(p1, p2):
    if p1 == p2[::-1]:
        return("É um palindromo")
        
    else:
        return "Não é um palindromo"
    
print(palindromo("amor", "roma"));

def DNAtest(string):
    bases = ["A", "T", "C", "G"]
    for letra in string:
        if letra not in bases:
            return False
        
    return True

print(DNAtest("ATXGTA"));


def DNAorRNA(string):
    bases_dna = ["A", "T", "C", "G"]
    bases_rna = ["A", "U", "C", "G"]

    for letra in string:
        if letra not in bases_dna and letra in bases_rna:
            return "RNA"
        
    return "DNA"

print(DNAorRNA("ATGTA"));

def DNAtoRNA(string):
    rna = ""
    for letra in string:
        if letra == "T":
            rna += "U"
        else:
            rna += letra
    return rna

def maxArea(altura):
    esquerda = 0
    direita = len(altura) - 1
    max_area = 0

    while esquerda < direita:
        area = min(altura[esquerda], altura[direita])
        largura = (direita - esquerda)
        max_area = max(max_area, area * largura)

        if altura[esquerda] < altura[direita]:
            esquerda += 1
        else:
            direita -= 1

    return max_area

test_height = [1,8,6,2,5,4,8,3,7]
print(maxArea(test_height));