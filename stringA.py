def contar_as(frase):
 
  frase_minuscula = frase.lower()

  contagem = frase_minuscula.count('a')

  return contagem

frase = input("Digite uma frase: ")

resultado = contar_as(frase)

if resultado ==1:
    print(f"A letra 'a' aparece {resultado} vez na frase.")
else:
    print(f"A letra 'a' aparece {resultado} vezes na frase.")