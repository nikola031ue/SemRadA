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
        print("Ustedeli ste " + str(row[4]) + " dinara.")


def prijava(ime, password, polozaj):
    query_vals = (ime, password, polozaj)
    command_handler.execute("SELECT * FROM korisnici WHERE ime = %s AND password = %s AND polozaj = %s", query_vals)

    result = command_handler.fetchall()
    return result


def registruj(ime, prezime, password, racun, polozaj):
    query_vals = (ime, prezime, password, racun, polozaj)
    command_handler.execute("INSERT INTO korisnici (ime, prezime, password, racun, polozaj) VALUES (%s,%s,%s,%s,%s)", query_vals)
    db.commit()

    if str(polozaj) == "1":
        print("Novi sluzbenik " + ime + " " + prezime + " je registrivan!")
    elif str(polozaj) == "2":
        print("Novi klijent " + ime + " " + prezime + " je registrivan!")
    else:
        print("Admin vec postoji!")




def brisanje(ime, prezime, racun, polozaj):
    query_vals = (ime, prezime, racun, polozaj)
    command_handler.execute("DELETE FROM korisnici WHERE ime = %s AND prezime = %s AND racun = %s AND polozaj = %s",
                            query_vals)
    db.commit()
    print(ime + " " + prezime + " je obrisan")


def trenutna_stednja(ime, prezime, racun, polozaj):
    query_vals = (ime, prezime, racun, polozaj)
    command_handler.execute("SELECT * FROM korisnici WHERE ime = %s AND prezime = %s AND racun = %s AND polozaj = %s",
                            query_vals)
    result = command_handler.fetchall()
    stanje = ""
    for row in result:
        stanje = row[4]
    return stanje


def update_stednja(ime, prezime, racun, polozaj, stednja):
    query_vals = (stednja, ime, prezime, racun, polozaj)
    sql = "UPDATE korisnici SET stednja = %s WHERE ime = %s AND prezime = %s AND racun = %s AND polozaj = %s"
    command_handler.execute(sql, query_vals)
    db.commit()


def svi_klijenti(polozaj):
    query_val = (polozaj, )
    sql = "SELECT * FROM korisnici WHERE polozaj = %s"
    command_handler.execute(sql, query_val)
    result = command_handler.fetchall()
    ime = []
    stanje = []
    for row in result:
        ime.append(row[0] + "\n" + row[1] + " " + str(row[5]))
        stanje.append(row[3])
    return ime, stanje


def svi_racuni():
    command_handler.execute("SELECT racun FROM korisnici")
    result = command_handler.fetchall()

    racuni = []
    for row in result:
        racuni.append(row)
    return racuni

