import matplotlib.pyplot as plt
import upiti as u


def graf(polozaj):
    ime, stanje = u.svi_klijenti(polozaj)
    plt.scatter(ime, stanje)
    plt.plot(ime, stanje)
    plt.xlabel('Ime')
    plt.xticks(rotation=90)
    plt.ylabel('Stanje')
    plt.title('Graf Klijentskih stanja')
    plt.show()

