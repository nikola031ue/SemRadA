import random
import upiti as u


def gen_racun():
    numbers = "0123456789"

    svi_racuni = u.svi_racuni()
    svi_racuni_lista = []
    length = 5
    racun = "".join(random.sample(numbers, length))
    for r in svi_racuni:
        svi_racuni_lista.append(r[0])

    while racun in svi_racuni_lista:
        racun = "".join(random.sample(numbers, length))

    return racun

