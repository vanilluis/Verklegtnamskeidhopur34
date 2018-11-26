def skra_vidskiptavin():
    pass

def fletta_vidskiptavin():
    pass
    
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

def pantanir_options():
    print("1. Skrá pöntun")
    print("2. Breyta pöntun")
    print("3. Fletta upp pöntun")
    print("4. Bakfæra pöntun")
    input_num = int(input("Val: "))


print("Veldu valmöguleika?")

print_options()
