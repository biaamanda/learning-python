# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite mais um numero: '))
# s = n1 +n2
# print(type(n1))

# print('A soma entre ', n1, ' e ', n2, ' vale ', s)
#print('A soma entre {} e {} vale {}'.format(n1, n2, s))

# faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele

info = input('Digite algo:')
print('O tipo primitivo desse valor é:', type(info))

print('Só tem espaços?', info.isspace())
print('É um número?', info.isnumeric())
print('É alfabético?', info.isalpha())
print('É alfanumérico?', info.isalnum())
print('Está em maiúsculas?', info.isupper())
print('Está em minúsculas?', info.islower())
print('Está capitalizada (primeira letra maiúscula)?', info.istitle())
