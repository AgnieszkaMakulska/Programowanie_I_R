m = float(input('Podaj masę ciała w kg: '))
h = float(input('Podaj wzrost w metrach: '))

BMI = m / h**2

print('BMI: ' + str(round(BMI,2)))

if BMI < 18.5:
    print('niedowaga')
elif BMI > 18.5 and BMI < 25:
    print("prawidłowa waga")
elif BMI > 25 and BMI < 30:
    print('nadwaga')
else:
    print('otyłość')