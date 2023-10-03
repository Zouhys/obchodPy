print("Vijtej v obchodnim centrum Mlada Boleslav")
run = True
nakup = [["Okurky", 0, 20],["Rajcata", 0, 10],["Papriky", 0, 10],["Lilie", 0, 30],["Ruze", 0, 25],["Tulipany", 0, 22],["Hoveziho - Kg", 0, 250],["Veproveho - Kg", 0, 200],["Kureciho - Kg ", 0, 180]]
cena_nakupu = 0
while run:
    rozhodnuti = int(input("Kam se vydas? Zelinarstvi - 1; Kvetinarstvi - 2; Reznik - 3; Opustit - 4 " ))
    if rozhodnuti == 1:
        while True : 
            print("vitej v zelinarstvi")
            print("mas na vyber: Okurky - 1; Rajcata - 2; Papriky - 3; exit - 4")
            vyber1 = int(input())
            if vyber1 == 1:
                print("kolik chces okurek?")
                po_okurek = int(input())
                nakup[0][1] += po_okurek
            if vyber1 == 2:
                print("kolik chces rajcat?")
                po_rajcat = int(input())
                nakup[1][1] += po_rajcat
            if vyber1 == 3:
                print("kolik chces parpik?")
                po_paprik = int(input())
                nakup[2][1] += po_paprik
            if vyber1 == 4:
                print("opustil jsi zelinarstvi")
                break

    elif rozhodnuti == 2:
        while True : 
            print("vitej v kvetinarstvi")
            print("mas na vyber: Lilie - 1; Ruze - 2; Tulipany - 3; exit - 4")
            vyber2 = int(input())
            if vyber2 == 1:
                print("kolik chces lilií?")
                po_li = int(input())
                nakup[3][1] += po_li
            if vyber2 == 2:
                print("kolik chces ruzi?")
                po_ru = int(input())
                nakup[4][1] += po_ru
            if vyber2 == 3:
                print("kolik chces tulipanu?")
                po_tul = int(input())
                nakup[5][1] += po_tul
            if vyber2 == 4:
                print("opustil jsi kvetinarstvi")
                break

    elif rozhodnuti == 3:
        while True : 
            print("vitej v reznictvi")
            print("mas na vyber: Hovezi - 1; Veprovy - 2; Kureci - 3; exit - 4")
            vyber3 = int(input())
            if vyber3 == 1:
                print("kolik chces hoveziho masa?")
                po_ho = int(input())
                nakup[6][1] += po_ho
            if vyber3 == 2:
                print("kolik chces veprovyho masa?")
                po_ve = int(input())
                nakup[7][1] += po_ve
            if vyber3 == 3:
                print("kolik chces kureciho masa?")
                po_kurec = int(input())
                nakup[8][1] += po_kurec
            if vyber3 == 4:
                print("opustil jsi reznika")
                break

    elif rozhodnuti == 4:
        print("opustil jsi obchodni centrum")
        print(f"tohle je v tvem nakupnim kosiku {nakup}")
        run = False
    else:
        print("neznam tento pozadavek")

for x in nakup :
     if not x[1] == 0: 
        vy = x[1] * x[2]
        cena_nakupu += vy
print(f"tohle je tva cena nakupu{cena_nakupu} kč")       

for y in nakup:
    if not y[1] == 0:
        print(f"{y[0]} {y[1]} krat - {y[1]* y[2]} kč ")
