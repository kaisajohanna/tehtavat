sukupuoli = input("Kerro sukupuolesi: ")
hemoglobiiniarvo = float(input("Mikä on hemoglobiinisi?"))

if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiinisi on alhainen.")
    elif hemoglobiiniarvo <= 175:
        print("Hemoglobiinisi on normaali.")
    else:
        print("Hemoglobiinisi on korkea.")

elif sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiinisi on alhainen.")
    elif hemoglobiiniarvo <= 195:
        print("Hemoglobiinisi on normaali.")
    else:
        print("Hemoglobiinisi on korkea.")