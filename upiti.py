import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", password="", database="banka")
command_handler = db.cursor(buffered=True)


def trenutno_stanje(ime, prezime, racun, polozaj):
    query_vals = (ime, prezime, racun, polozaj)
    command_handler.execute("SELECT * FROM korisnici WHERE ime = %s AND prezime = %s AND racun = %s AND polozaj = %s",
                            query_vals)
    result = command_handler.fetchall()
    stanje = ""
    for row in result:
        stanje = row[3]
    return stanje


def update_stanje(ime, prezime, racun, polozaj, stanje):
    query_vals = (stanje, ime, prezime, racun, polozaj)
    sql = "UPDATE korisnici SET stanje = %s WHERE ime = %s AND prezime = %s AND racun = %s AND polozaj = %s"
    command_handler.execute(sql, query_vals)
    db.commit()


def ispisi_klijenta(ime, prezime, racun, polozaj):
    query_vals = (ime, prezime, racun, polozaj)
    sql = "SELECT * FROM korisnici WHERE ime = %s AND prezime = %s AND racun = %s AND polozaj = %s"
    command_handler.execute(sql, query_vals)

    result = command_handler.fetchall()

    for row in result:
        print(row[0] + " " + row[1] + " ima na stanju " + str(row[3]) + " dinara")


def prijava(ime, password, polozaj):
    query_vals = (ime, password, polozaj)
    command_handler.execute("SELECT * FROM korisnici WHERE ime = %s AND password = %s AND polozaj = %s", query_vals)

    result = command_handler.fetchall()
    return result


def registruj(ime, prezime, password, polozaj):
    query_vals = (ime, prezime, password, polozaj)
    command_handler.execute("INSERT INTO korisnici (ime, prezime, password, polozaj) VALUES (%s,%s,%s,%s)", query_vals)
    db.commit()
    korisnik = ""
    if polozaj == "1":
        korisnik = "sluzbenik"
    elif polozaj == "2":
        korisnik = "klijent"
    else:
        print("Admin vec postoji!")

    print("Novi " + korisnik + " " + ime + " " + prezime + " je registrivan")


def brisanje(ime, prezime, polozaj):
    query_vals = (ime, prezime, polozaj)
    command_handler.execute("DELETE FROM korisnici WHERE ime = %s AND prezime = %s AND polozaj = %s",
                            query_vals)
    db.commit()
    print(ime + " " + prezime + " je obrisan")
