from tabulate import tabulate
import itertools as it

def converter(bilangan, pembagi):
    hasil = []
    hasilbilangan =""
    i = True
    while i :
        if bilangan >= pembagi :
            hasil.append(bilangan)
            sisa = bilangan % pembagi
            bilangan = bilangan // pembagi
            if sisa > 9 :
                huruf = hexaAppear(sisa)
                hasilbilangan += huruf
                sisa = "{0} = {1}".format(sisa, huruf)
            else :
                hasilbilangan += str (sisa)
            divid = "{0}------ {1}".format(pembagi, sisa)
            hasil.append(divid)
        else :
            if bilangan > 9:
                bilangan = hexaAppear(bilangan)
            hasilbilangan += str(bilangan)
            hasil.append(bilangan)
            i = False
            break
        hasil.append("")
    hasilbilangan = "".join(reversed(hasilbilangan))
    return (hasil, hasilbilangan)

def hexaAppear (bilangan):
    if bilangan == 10 :
        return "A"
    elif bilangan == 11 :
        return "B"
    elif bilangan == 12:
        return "C"
    elif bilangan == 13:
        return "D"
    elif bilangan == 14:
        return "E"
    elif bilangan == 15: 
        return "F"
    elif bilangan == 16:
        return "G"
    
    bilangan = int (input("Masukkan bilangan untuk dikonversi:"))
    print("==================================================")

    biner, hasilBiner = converter(bilangan, 2)
    octal, hasilOctal = converter(bilangan, 8)
    hexa, hasilHexa = converter(bilangan, 16)

    combine = list(it.zip_longest(biner, octal, hexa))

    header = ("Binner", "Octal", "Hexadecimal")

    print(tabulate(combine, header, tablefmt="plain"))
    print("")
    print("====================================")
    print("Binner :",hasilBiner, "   Octal :",hasilOctal, "   Hexa :",hasilHexa)
    