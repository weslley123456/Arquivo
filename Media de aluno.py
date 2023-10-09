n1=float (input('informe o valor da sua primeia nota:'))
n2=float (input('informe o valor da sua segunda nota:'))
n3=float (input('informe o valor da sua tervceira nota:'))
n4=float (input('informe o valor da sua quarta nota:'))
m=(n1+n2+n3+n4)/4
if m>=7:
    print (f'sua media foi de {m}, parabens voçê foi aprovado')
elif(m<7) and (m>=5.5):
    print (f'sua media foi de {m}, voce esta de recuperação!')
else:
    print (f'sua media foi de {m}, abaixo da mdeia, voce esta reprovado')