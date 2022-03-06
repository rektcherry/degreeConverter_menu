import sys
def menu():
    while True:
        print('What do you want to convert?')
        print('1) Celsius -> Fahrenheit')
        print('2) Celsius -> Kelvin')
        print('3) Fahrenheit -> Kelvin')
        print('4) Fahrenheit -> Celsius')
        print('5) Kelvin -> Celsius')
        print('6) Kelvin -> Fahrenheit')
        print('0) End')
        nro=int(input('Your choise: '))
        return nro

def main():
    
    import lampotila
    while True:
        uinput = menu()
        if uinput == 1:
            degree=float(input(('Give degree: ')))
            result=lampotila.c2f(degree)
            print('Degree in fahrenheit: ',round(result,2))
            continue
        if uinput == 2:
            degree=float(input(('Give degree: ')))
            result=lampotila.c2k(degree)
            print('Degree in kelvin: ',round(result,2))
            continue
        if uinput == 3:
            result = float(input(('Give degree: ')))
            tulos = lampotila.f2k(degree)
            print('Degree in kelvin: ',round(result,2))
            continue
        if uinput == 4:
            degree = float(input(('Give degree: ')))
            result = lampotila.f2c(degree)
            print('Degree in celsius: ',round(result,2))
            continue
        if uinput == 5:
            degree = float(input(('Give degree: ')))
            result=lampotila.k2c(degree)
            print('Degree in celsius: ',round(result,2))
            continue
        if uinput == 6:
            degree=float(input(('Give degree: ')))
            result=lampotila.k2f(degree)
            print('Degree in fahrenheit: ',round(result,2))
            continue
        if uinput==0:
            sys.exit('System exit.')
main()            
            
