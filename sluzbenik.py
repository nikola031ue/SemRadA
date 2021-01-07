import upiti as u
import graf as g
import generator_racuna as gr


def sluzbenik_session():
    while 1:
        print("")
        print("Sluzbenik meni")
        print("1. Registruj novog Klijenta")
        print("2. Obrisi Klijenta")
        print("3. Dodaj novac na racun")
        print("4. Transakcije")
        print("5. Graf Klijentskih stanja")
        print("6. Odjavi se")

        izbor = input(str("Izbor: "))
        if izbor == "1":
            print("")
            print("Regiturj novog Klijenta")
            print("")
            ime = input(str("Ime klijenta: "))
            prezime = input(str("Prezime Klijenta: "))
            password = input(str("Lozinka Klijenta: "))
            polozaj = 2
            racun = gr.gen_racun()
            u.registruj(ime, prezime, password, racun, polozaj)
        elif izbor == "2":
            print("")
            print("Obrisi Klijenta")
            print("")
            ime = input(str("Ime Klijenta: "))
            prezime = input(str("Prezime Klijenta: "))
            racun = input(str("Racun Klijenta: "))
            polozaj = 2
            u.brisanje(ime, prezime, racun, polozaj)
        elif izbor == "3":
            print("")
            print("Dodaj novac na racun")
            print("")
            ime = input(str("Ime Klijenta: "))
            prezime = input(str("Prezime Klijenta: "))
            racun = input(str("Broj racuna Klijenta: "))
            kolicina: float = float(input("Kolicina novca: "))
            polozaj = 2

            trenutno_stanje = u.trenutno_stanje(ime, prezime, racun, polozaj)
            za_stednju = kolicina/100*5
            za_stanje = kolicina - za_stednju
            stanje = trenutno_stanje + za_stanje
            u.update_stanje(ime, prezime, racun, polozaj, stanje)

            trenutna_stednja = u.trenutna_stednja(ime, prezime, racun, polozaj)
            stednja = trenutna_stednja + za_stednju
            u.update_stednja(ime, prezime, racun, polozaj, stednja)
            u.ispisi_klijenta(ime, prezime, racun, polozaj)
        elif izbor == "4":
            print("")
            print("Transakcije izmedju Klijenata")
            print("")
            ime_posiljaoca = input(str("Ime Klijenta posiljaoca: "))
            prezime_posiljaoca = input(str("Prezime Klijenta posiljaoca: "))
            racun_posiljaoca = input(str("Broj racuna Kijenta posiljaoca: "))
            polozaj = 2
            ime_primaoca = input(str("Ime Klijenta primaoca: "))
            prezime_primaoca = input(str("Prezime Klijenta primaoca: "))
            racun_primaoca = input(str("Broj racuna Klijenta primaoca: "))

            trenutno_stanje_posiljaoca = u.trenutno_stanje(ime_posiljaoca, prezime_posiljaoca, racun_posiljaoca, polozaj)
            trenutno_stanje_primaoca = u.trenutno_stanje(ime_primaoca, prezime_primaoca, racun_primaoca, polozaj)

            kolicina_za_transakciju = (float(input("Kolicina novca za transakciju: ")))

            if trenutno_stanje_posiljaoca < kolicina_za_transakciju:
                print("Nemate dovoljno novca na racunu!")
                break
            za_stednju = kolicina_za_transakciju/100*5
            za_transakciju = kolicina_za_transakciju - za_stednju

            trenutno_stanje_posiljaoca = trenutno_stanje_posiljaoca - kolicina_za_transakciju
            trenutno_stanje_primaoca = trenutno_stanje_primaoca + za_transakciju
            trenutna_stednja_primaoca = u.trenutna_stednja(ime_primaoca, prezime_primaoca, racun_primaoca, polozaj)
            trenutna_stednja_primaoca = trenutna_stednja_primaoca + za_stednju

            u.update_stanje(ime_posiljaoca, prezime_posiljaoca, racun_posiljaoca, polozaj, trenutno_stanje_posiljaoca)
            u.update_stanje(ime_primaoca, prezime_primaoca, racun_primaoca, polozaj, trenutno_stanje_primaoca)

            u.update_stednja(ime_primaoca, prezime_primaoca, racun_primaoca, polozaj, trenutna_stednja_primaoca)

            print("Klijent posiljaoca:")
            u.ispisi_klijenta(ime_posiljaoca, prezime_posiljaoca, racun_posiljaoca, polozaj)
            print("")
            print("Klijent primaoc: ")
            u.ispisi_klijenta(ime_primaoca, prezime_primaoca, racun_primaoca, polozaj)
        elif izbor == "5":
            print("")
            print("Graf Klijentskih stanja")
            print("")
            polozaj = 2
            g.graf(polozaj)
        elif izbor == "6":
            break
        else:
            print("Pogresan izbor")


def auth_sluzbenik():
    print("")
    print("Sluzbenik login")
    print("")

    ime = input(str("Ime: "))
    password = input(str("Lozinka: "))
    polozaj = 1
    result = u.prijava(ime, password, polozaj)
    for row in result:

        if ime == row[0]:
            if password == row[2]:
                print("Uspeh")
                sluzbenik_session()
            else:
                print("Netacna lozinka")
        else:
            print("Pogresno ime ili lozinka")
