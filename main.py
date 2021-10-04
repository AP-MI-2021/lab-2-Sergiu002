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

def test_get_temp():
    print("Adaugati o temperatura, scara temperaturi si scara in care vreti sa convertiti temperatura")
    tmp = int(input("Dati un numar. "))
    scara1 = input("Scrie-ti unitatea de masura a temperaturii. ")
    scara2 = input("Scrie-ti unitatea de masura in care doriti sa comvertiti temperatura. ")
    result = get_temp(tmp, scara1, scara2)

    assert get_temp(237, 'C', 'K') == 510.15
    print(result)
print(test_get_temp())
def cmmdc(Var1, Var2):
    res = Var1 % Var2
    while res:
        Var1 = Var2
        Var2 = res
        res = Var1 % Var2
    return Var2

def cmmmc(Var1, Var2):
    return Var1 * Var2 // cmmdc(Var1, Var2)

def get_cmmmc(list):
    aux = 1
    for index in list:
        aux = cmmmc(index, aux)
    return aux

def test_get_cmmmc():
    List = []
    number = int(input("Introduceti numarul elementelor"))
    for index in range(0, number):
        Elem = int(input())
        List.append(Elem)
    print(get_cmmmc(List))
print(test_get_cmmmc())