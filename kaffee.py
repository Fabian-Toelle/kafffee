print("Hello, welcome to my new Coffee-shop")
print("--------------------------------------------------------------------")

# vareable
latte = "Latte: 8€"
cappucino = "Cappucino: 9€"
esspresso = "Esspresso: 6€"
black_coffee = "Schwarzer Kaffee: 5€"
menu2 = "\n" + latte + "\n" + cappucino + "\n" + esspresso + "\n" + black_coffee + "\n"

name = input("Was ist dein name?: ")
input("Hallo " + name + ", was für ein Kaffee möchtest du heute Trinken? Hir ist was wir verkaufen: " + "\n" + menu2)

while True:
    eingabe = input("Gebe deine bestellung ein: ")
    if eingabe == "Latte":
        print("Das macht dann 8€")
        print("Hir bitte ihr getränk!")
    break

while True:
    if eingabe == "Cappucino":
        print("Das macht dann: 9€")
        print("Hir bitte ihr getränk!")
    break

while True:
    if eingabe == "Esspresso":
        print("Das macht dann 6€")
        print("Hir bitte ihr getränk!")
    break

while True:
    if eingabe == "Schwarzen Kaffee":
        print("Das macht dann 5€")
        print("Hir bitte ihr getränk!")
    break
print("--------------------------------------------")

eingabe2 = input("[Y/n] wars das?")
yj = "Y"
nj = "n"

while True == yj:
    if eingabe2 == True:
        print("Programmende")
        print("-----------Danke für das nutzen des Programm´s-----------")
        input("Drücke ein beliebege taste um das Programm zu beenden... ")
    break
    break

while False == nj:
    if eingabe2 == False == nj:
        input("Was möchten sie denn noch bestellen? hir ist unser menu.")
        input(menu2)
    break

while False == nj:
    eingabe3 = input("Geben ein was doch noch haben möchtest: ")
    if eingabe3 == "Latte":
        print("Das macht dann 8€")
        print("Hir bitte ihr getränk!")
    break

while False == nj:
        if eingabe3 == "Cappucino":
            print("Das macht dann: 9€")
            print("Hir bitte ihr getränk!")
        break

while False == nj:
    if eingabe3 == "Esspresso":
        print("Das macht dann 6€")
        print("Hir bitte ihr getränk!")
    break

while False == nj:
    if eingabe3 == "Schwarzen Kaffee":
        print("Das macht dann 5€")
        print("Hir bitte ihr getränk!")
    break