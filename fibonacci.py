def pertence_fibonacci(numero):
 
  a = 0
  b = 1
  
  while b < numero:
    a, b = b, a + b
  return b == numero

numero_informado = int(input("Digite um número: "))
if pertence_fibonacci(numero_informado):
  print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")