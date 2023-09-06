année = int(input("Entrez votre année : \n>").strip())


if année % 4 == 0 and année % 400 < 100:
    print("Bissextile")
else:
    print("Non bissextile")