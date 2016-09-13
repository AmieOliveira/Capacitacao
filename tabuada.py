s='Esse programa fornece a tabuada de qualquer númeroentre 1 e 10. Se quiser sair, digite "nao" ao fim do programa.\n'
for j in range(0,len(s),50):
    print s[j:j+50]+'\n',

pergunta='Sim'
sim='Sim'
nao="Nao"
while pergunta=='Sim':
    n=input('Digite um número entre 1 e 10:')
    if n<1 or n>10: n=input('Digite um número entre 1 e 10:')
    else: print '\n'
    for i in range(11):
        print n,'*',i,'=',n*i
    print '\n'
    pergunta=input('Quer continuar?')
