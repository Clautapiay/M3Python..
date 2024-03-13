def calculo_de_promedio(velocidades):
#Calcular promedio de lista de velocidades.

  suma = 0
  for velocidad in velocidades:
    suma += velocidad

  promedio = suma / len(velocidades)
  return promedio


def correas_sobre_promedio(velocidades):

  #Tener en cuenta las posiciones de los valores sobre el promedio.

  promedio = calculo_de_promedio(velocidades)
  posiciones_sobre_promedio = []

  for i, velocidad in enumerate(velocidades):
    if velocidad > promedio:
      posiciones_sobre_promedio.append(i)

  return posiciones_sobre_promedio


velocidades = [25, 12, 19, 16, 11, 11, 24, 1,
              14, 14, 16, 10, 6, 23, 13, 25, 4,
              19, 14, 20, 18, 9, 18, 4, 18, 1, 3,
              4, 2, 14, 23, 19, 23, 9, 18, 20, 22,
              14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12,
              20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

promedio = calculo_de_promedio(velocidades)
print("Promedio de velocidades:", promedio)

posiciones_sobre_promedio = correas_sobre_promedio(velocidades)
print("Posiciones de las correas sobre el promedio:", posiciones_sobre_promedio)
