def get_temp(tmp, scara1, scara2):
    """
    Unitatiile de masura disponibile pentru temperatura(K, F, C)
    Acest program converteste o temperatura data dintr-o unitate de masura
    in alta unitate de masura
    :param tmp: float
    :param scara1: string
    :param scara2: string
    :return: float (returneaza temepratura tmp convertita din scara1 in scara2)
    """

    if scara1 == 'C' and scara2 == 'F':
        return 1.8000 * tmp + 32
    elif scara1 == 'C' and scara2 == 'K':
        return tmp + 273.15
    elif scara1 == 'K' and scara2 == 'F':
        return tmp * 9 // 5 - 459.67
    elif scara1 == 'K' and scara2 == 'C':
        return tmp - 273.15
    elif scara1 == 'F' and scara2 == 'C':
        return (tmp - 32) // 1.8000
    elif scara1 == 'F' and scara2 == 'K':
        return tmp + 459.67 // (9 // 5)
    elif scara1 == 'F' and scara2 == 'F' or scara1 == 'C' and scara2 == 'C' or scara1 == 'K' and scara2 == 'K':
        return tmp

def test_get_temp():
    """
    Testeaza daca funtia get_temp functioneaza
    """
    assert get_temp(237, 'C', 'K') == 510.15
    assert get_temp(345, 'C', 'K') == 618.15
    assert get_temp(78, 'F', 'C') == 25.0
test_get_temp()

def get_cmmmc(list):
    """
    Acest program caluleaza cel mai mic multiplu comun a n numere date
    :param list: integer
    :return: integer (Returneaza cel mai mic multiplu comun)
    """
    aux = 1
    for index in list:
        copie1 = index
        copie2 = aux
        res = copie1 % copie2
        while res:
            copie1 = copie2
            copie2 = res
            res = copie1 % copie2
        aux = index * aux // copie2
    return aux

def test_get_cmmmc():
    """
    Testeaza daca funtia get_cmmmc functioneaza
    """
    assert(get_cmmmc([1, 2, 3, 4, 5])) == 60
    assert(get_cmmmc([1, 5, 6, 3])) == 30
test_get_cmmmc()

def is_palindrome(var1):
    """
    Testeaza daca var1 este palindrom
    :param var1: integer
    :return: bool (returneaza True daca var1 este palindrom si False daca var1 nu este palindrom
    """
    aux  = var1
    oglindit = 0
    while aux:
        cif = aux % 10
        oglindit = oglindit * 10 + cif
        aux = aux // 10
    if oglindit == var1:
        return True
    else:
        return False
def test_is_palindrom():
    """
    Testeaza daca functia is_palindrom funtioneaza
    """
    assert(is_palindrome(121)) is True
    assert(is_palindrome(123)) is False
    assert(is_palindrome(565565)) is True
test_is_palindrom()
def main():
    """
    Aceasta este interfata utilizatorului
    """
    problema = int(input("Alege problema dorita: 5, 13 sau 14 "))
    if problema == 13:
        gasit = True
        while gasit == True:
            print("Adaugati o temperatura, scara temperaturi si scara in care vreti sa convertiti temperatura")
            tmp = int(input("Dati o temperatura. "))
            scara1 = input("Scrie-ti unitatea de masura a temperaturii. ")
            scara2 = input("Scrie-ti unitatea de masura in care doriti sa comvertiti temperatura. ")
            result = get_temp(tmp, scara1, scara2)
            print(result)
            continua = input("Continuati? DA sau NU ")
            if continua == 'NU':
                gasit = False
                main()
    elif problema == 14:
        gasit = True
        while gasit:
            List = []
            number = int(input("Introduceti numarul elementelor"))
            for index in range(0, number):
                Elem = int(input())
                List.append(Elem)
            print(get_cmmmc(List))
            continua = input("Continuati? DA sau NU ")
            if continua == 'NU':
                gasit = False
                main()
    elif problema == 5:
        gasit = True
        while gasit:
            numar = int(input("Introduceti un numar: "))
            print(is_palindrome(numar))
            continua = input("Continuati? DA sau NU ")
            if continua == 'NU':
                gasit = False
                main()
if __name__ == '__main__':
    main()