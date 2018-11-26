def print_options():
    print("1.  Viðskiptavinir")
    print("2.  Bílafloti")
    print("3.  Afgreiðsla")
    print("4.  Pantanir")
    input_num = int(input("Val: "))
    if input_num == 1:
        vidskiptavinir_options()
    elif input_num == 2:
        bilafloti_options()
    elif input_num == 3:
        afgreidsla_options()
    elif input_num == 4:
        pantanir_options()
    else:
        print_options()

def vidskiptavinir_options():
    print("1.  Skrá nýjan viðskiptavin")
    print("2.  Fletta upp viðskiptavin")
    print("3.  Afskrá viðskiptavin")
    print("4.  Uppfæra viðskiptavin")
    print("5.  Setja á bannlista")
    print("6.  Taka af bannlista")
    print("7.  Sekta viðskiptavin")
    input_num = int(input("Val: "))
    if input_num == 1:
        skra_vidskiptavin()
    elif input_num == 2:
        fletta_vidskiptavin()
    elif input_num == 3:
        afskra_vidskiptavin()
    elif input_num == 4:
        breyta_vidskiptavin()
    elif input_num == 5:
        setja_a_bannlista()
    elif input_num == 6:
        taka_af_bannlista()
    elif input_num == 7:
        sekta_vidskiptavini()

def skra_vidskiptavin():
    nafn = input("Nafn: ")
    kennitala = input("Kennitala: ")

def afskra_vidskiptavin():
    kt = input("Hvern a að afskrá? (kennitala) ")
    confirm = input("Afskra: Johana Einarsdottir, {}? (y/n)".format(kt))
    if(confirm == "y"):
        print("Afskráð")
    else:
        print("Hætt við")

def fletta_vidskiptavin():
    pass


def bilafloti_options():
    print("1.  Birta lausa bíla")
    print("2.  Birta útleigða bíla")
    print("3.  Skila bíl")
    print("4.  Skrá bíl")
    print("5.  Afskrá bíl")
    print("6.  Leita að bíl")
    print("7.  Bilaðir bílar")
    input_num = int(input("Val: "))
    if input_num == 1:
        birta_lausa_bila()
    elif input_num == 2:
        birta_utleigda_bila()
    elif input_num == 3:
        skila_bil()
    elif input_num == 4:
        skra_bil()
    elif input_num == 5:
        afskra_bil()
    elif input_num == 6:
        leita_ad_bil()
    elif input_num == 7:
        biladir_bilar()

def birta_lausa_bila():
    print("SB-463, 1998, jeppi, rauður, 4500 kr/dag")
    print("EU-N45, 2014, smábíll, grár, 2500 kr/dag")

def birta_utleigda_bila():
    print("SX-452, 2003, jeppi, grænn, 3000 kr/dag")

def skila_bil():
    bilnumer = input("Bílnúmer: ")
    print("Bílnum {} hefur verið skilað!".format(bilnumer))

def skra_bil():
    bilnumer = input("Bílnúmer: ")
    print("Bíllinn {} hefur verið skráður!".format(bilnumer))

def afgreidsla_options():
    print("1.  Birta lausa bíla")
    print("2.  Skrá nýjan viðskiptavin")
    print("3.  Skrá pöntun")
    print("4.  Kostnaðarmat")
    print("5.  Skila bíl")
    print("6.  Afskrá viðskiptavin")
    print("7.  Bakfæra pöntun")
    print("8.  Uppfæra viðskiptavin") 
    print("9.  Breyta pöntun")
    input_num = int(input("Val: "))
    if input_num == 1:
        birta_lausa_bila()
    elif input_num == 2:
        skra_vidskiptavin()
    elif input_num == 3:
        skra_pontun()
    elif input_num == 4:
        kostnadarmat()
    elif input_num == 5:
        skila_bil()
    elif input_num == 6:
        afskra_vidskiptavin()
    elif input_num == 7:
        bakfaera_pontun()
    elif input_num == 8:
        breyta_vidskiptavin()
    elif input_num == 9:
        breyta_pontun()

def pantanir_options():
    print("1. Skrá pöntun")
    print("2. Breyta pöntun")
    print("3. Fletta upp pöntun")
    print("4. Bakfæra pöntun")
    input_num = int(input("Val: "))
    if input_num == 1:
        skra_pontun()
    elif input_num == 2:
        breyta_pontun()
    elif input_num == 3:
        fletta_pontun()
    elif input_num == 4:
        bakfaera_pontun()

def fletta_pontun():
    kt = input("Hver er kennitalan?")
    print("Þín pöntun er frá 10/12/18 til 14/12/18 á rauðan jeppa, SB-463")


print("Veldu valmöguleika?")

print_options()
