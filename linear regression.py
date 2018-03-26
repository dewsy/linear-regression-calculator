import os


def clear(): return os.system('cls')


xi = []
yi = []

reqest = []
estim = []


def printtop():
    clear()
    print("Independent values: ", xi)
    print("Dependent pairs: ", yi)
    print("Requested independent values: ", reqest)
    print("Estimated dependent pairs: ", estim, "\n\n\n")


def inputter(x):
    x.append(input('Add a value to the list: '))
    if isNumber(x[len(x) - 1]) == 'delete':
        print("That's not a number, i'm deleting it")
        del(x[len(x) - 1])
        inputter(x)
    elif isNumber(x[len(x) - 1]) == 'calculate':
        del(x[len(x) - 1])
        return 'calculate'


def isNumber(x):
    if x == 'x':
        return 'calculate'
    else:
        try:
            int(x)
        except ValueError:
            return 'delete'


k = 0
printtop()
print('Now we are collecting the known data pairs:')
while True:
    if k < 3:
        pass
    else:
        print('you can finish input by typing x')
    print('Independent')
    if inputter(xi) == 'calculate':
        break
    printtop()
    print('dependent:')
    if inputter(yi) == 'calculate':
        print('You can not quit at this stage')
        inputter(yi)
    printtop()
    k = k + 1

xi = [int(x) for x in xi]
yi = [int(x) for x in yi]

xavr = sum(xi) / len(xi)
yavr = sum(yi) / len(yi)

xMinAvr = [x - xavr for x in xi]
yMinAvr = [y - yavr for y in yi]

xMinAvr = [round(x) for x in xMinAvr]
yMinAvr = [round(y) for y in yMinAvr]

times = []
x = 0
while x < len(xMinAvr):
    times.append(xMinAvr[x] * yMinAvr[x])
    x = x + 1

squared = [x * x for x in xMinAvr]

b1 = round(sum(times) / sum(squared))

b0 = round(yavr - b1 * xavr)

printtop()
while True:
    try:
        print('\nFrom now on, you can exit if you type in any letter!')
        z = int(
            input('Give me an independent value to estimate its dependent pair!\n'))
        reqest.append(z)
        printtop()
        t = b0 + b1 * z
        estim.append(t)
        printtop()
        print("The estimation is: ", t)
    except ValueError:
        printtop()
        print('Goodbye!')
        break
