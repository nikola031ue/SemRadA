import admin as a
import sluzbenik as s
import klijent as k


def main():
    while 1:
        print("DOBRODOSLI U BANKU")
        print("")
        print("1. Prijavi se kao admin")
        print("2. Prijavi se kao sluzbenik")
        print("3. Prijavi se kao klijent")
        print("4. Odjavi se")

        izbor = input(str("Izbor: "))
        if izbor == "1":
            print("Admin")
            a.auth_admin()
        elif izbor == "2":
            print("Sluzbenik")
            s.auth_sluzbenik()
        elif izbor == "3":
            print("Klijent")
            k.auth_klijent()
        elif izbor == "4":
            break
        else:
            print("Nepostojeci izbor")


main()
