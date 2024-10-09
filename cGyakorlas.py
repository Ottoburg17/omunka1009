def harom():
    # 1. megoldás
    for i in range(0,21,1):
        print(i)

    # 2. megoldás
    for i in range(21):
        print(i)

    #3. megoldás
    for i in range(0,21):
        print(i)

    #4.megoldás
    i = 0
    while i<21:
        print(i)
        i+=1
def negy():
    for i in range(20,57,2):
        print(i)

def ot():
    for i in range(77,-77,-4):
        print(i)

def beolvas():
    szam = int(input("Kérem adjon meg egy egész számot!"))
    return szam

def hat():
    #6.	Kérj be 2 számot, majd írasd ki a számokat a legkisebbtől a legnagyobbig! (a legnagyobbat is! Ha az első szám nagyobb, abban az esetben is a legkisebbtől a legnagyobbig írasd ki!)

    szam1 = beolvas()
    szam2 = beolvas()

    # melyik a nagyobb
    if szam2 < szam1:
        # csere
        atmenet = szam1
        szam1=szam2
        szam2 = atmenet

    for i in range(szam1, szam2+1, 1):
        print(i, end=" ")


def het():
    #7.	Kérj be 2 számot, majd írasd ki a számokat 0-tól a 2 szám szorzatáig!
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    if szorzat<0:
        for i in range(0, szorzat-1,-1):
            print(i, end=" ")
    else:
        for i in range(0, szorzat+1,1):
            print(i, end=" ")
def kilenc():
    for i in range(1, 8):  # 1-től 7-ig
        if i < 7:
            print(i, end=", ")
        else:
            print(i)
def faktorialis(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def tizes():
    szam = beolvas()
    eredmeny = faktorialis(szam)
    print(f"A {szam} faktoriálisa: {eredmeny}")


def beolvas():
    szam = int(input("Kérem adjon meg egy egész számot: "))
    return szam


def tizenegy():
    x = beolvas()
    y = beolvas()

    eredmeny = 3 * x + (y ** 2)  # Kiszámítja a kifejezést
    print(f"3 * {x} + {y}^2 = {eredmeny}")


def beolvas():
    szam = int(input("Kérem adjon meg egy egész számot: "))
    return szam


def tizenkettő():
    szam1 = beolvas()
    szam2 = beolvas()

    # A legkisebb és legnagyobb szám meghatározása
    also = min(szam1, szam2)
    felso = max(szam1, szam2)

    paros_db = 0
    for i in range(also, felso + 1):
        if i % 2 == 0:  # Ellenőrizzük, hogy páros szám-e
            paros_db += 1

    print(f"A {also} és {felso} közötti páros számok száma: {paros_db}")