#Exercise 177: Roman Numerals
'''(25 Lines)
As the name implies, Roman numerals were developed in ancient Rome. Even after
the Roman empire fell, its numerals continued to be widely used in Europe until the
late middle ages, and its numerals are still used in limited circumstances today.
Roman numerals are constructed from the letters M, D, C, L, X, V and I which
represent 1000, 500, 100, 50, 10, 5 and 1 respectively. The numerals are generally
written from largest value to smallest value. When this occurs the value of the number
is the sum of the values of all of its numerals. If a smaller value precedes a larger
value then the smaller value is subtracted from the larger value that it immediately
precedes, and that difference is added to the value of the number.
Create a recursive function that converts a Roman numeral to an integer. Your
function should process one or two characters at the beginning of the string, and
then call itself recursively on all of the unprocessed characters. Use an empty string,
which has the value 0, for the base case. In addition, write a main program that reads
a Roman numeral from the user and displays its value. You can assume that the value
entered by the user is valid. Your program does not need to do any error checking.'''

print('Exercício 177: Vamos converter um número em romano para decimal.')

def romano(n, fin=0):
    dic = {"M":1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    if len(n) == 1:
        fin += dic[n]
    else:
        if dic[n[0]] < dic[n[1]]:
            fin = fin - dic[n[0]] + romano(n[1:len(n)], fin)
        else:
            fin += dic[n[0]] + romano(n[1:len(n)], fin)

    return fin

def main():
    num = str(input("Digite o número em romano a ser convertido: "))
    num = num.upper()
    num = num.replace(' ', '')
    res = romano(num)
    print("o número romano", num, "corresponde a", res, "em decimal.\n")

main()
