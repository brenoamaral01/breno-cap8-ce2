#Exercise 175: Recursive Decimal to Binary
'''(34 Lines)
In Exercise 82 you wrote a program that used a loop to convert a decimal number
to its binary representation. In this exercise you will perform the same task using
recursion.
Write a recursive function that converts a non-negative decimal number to binary.
Treat 0 and 1 as base cases which return a string containing the appropriate digit. For
all other positive integers, n, you should compute the next digit using the remainder
operator and then make a recursive call to compute the digits of n // 2. Finally, you
should concatenate the result of the recursive call (which will be a string) and the
next digit (which you will need to convert to a string) and return this string as the
result of the function.
Write a main program that uses your recursive function to convert a non-negative
integer entered by the user from decimal to binary. Your program should display an
appropriate error message if the user enters a negative value.'''

print('Exercício 175: Vamos converter um inteiro não negativo em binário.')

def dec_bin(n, palavra=''):
    if n == 1:
        add = '1'
        palavra = palavra + add
    elif n == 0:
        palavra = '0'
    else:
        add = n%2
        palavra = str(dec_bin(round(n/2 - 0.1), palavra)) + str(add)

    return palavra

def main():
    cor = False
    while cor == False:
        cor = True
        num = int(input("Digite um inteiro não negativo a ser convertido: "))
        if num < 0:
            cor = False
            print("Este número não pode ser convertido por ser negativo. Tente novamente.")

    res = dec_bin(num)
    print("O inteiro", num, "em binário é", res, '\n')

main()
