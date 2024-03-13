#Funcion factorial
def calculo_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculo_factorial(n-1)
    

#Funcion productoria
def calculo_productoria(lista):
    productoria = 1
    for elemento in lista:
        productoria *= elemento
    return productoria

#Calculo
def calculo(**kwargs):
    for key, value in kwargs.items():
        if "fact" in key:
            print(f"El factorial de {value} es {calculo_factorial(value)}")
        elif "prod" in key:
            print(f"La productorial de {value} es {calculo_productoria(value)}")

if __name__ == "__main__":
    calculo(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)
