padres = {
    "carla":"juan",
    "jose":"juan",
    "agustin":"juan",
    "mateo":"agustin",
    "luis":"jose"
}

madres = {
    "carla":"maria",
    "jose":"maria",
    "agustin":"maria",
    "mateo":"sofia",
    "luis":"ana"
}

def obtener_padre(persona):
    return padres.get(persona)


def obtener_madre(persona):
    return madres.get(persona)

def es_abuelo(abuelo, nieto):
    padre_del_nieto = obtener_padre(nieto)
    madre_del_nieto = obtener_madre(nieto)

    if padre_del_nieto is not None:
        if obtener_padre(padre_del_nieto) == abuelo:
            return True

        if obtener_madre(padre_del_nieto) == abuelo:
            return True

    if madre_del_nieto is not None:
        if obtener_padre(madre_del_nieto) == abuelo:
            return True

        if obtener_madre(madre_del_nieto) == abuelo:
            return True

    return False


def obtener_hermanos(persona):
    hermanos = []

    padre = obtener_padre(persona)
    madre = obtener_madre(persona)

    personas = set(padres.keys()) | set(madres.keys())

    for otra_persona in personas:
        if otra_persona == persona:
            continue

        mismo_padre = (
            padre is not None
            and obtener_padre(otra_persona) == padre
        )

        misma_madre = (
            madre is not None
            and obtener_madre(otra_persona) == madre
        )

        if mismo_padre or misma_madre:
            hermanos.append(otra_persona)

    return hermanos

def es_tio(tio, sobrino):
    padre = obtener_padre(sobrino)
    madre = obtener_madre(sobrino)

    if padre is not None:
        if tio in obtener_hermanos(padre):
            return True

    if madre is not None:
        if tio in obtener_hermanos(madre):
            return True

    return False

print("¿Juan es abuelo de Sofía?")
print(es_abuelo("juan", "sofia"))

print()

print("¿María es abuela de Sofía?")
print(es_abuelo("maria", "sofia"))

print()

print("Hermanos de agustin:")
print(obtener_hermanos("agustin"))

print()

print("¿Ana es tía de Sofía?")
print(es_tio("ana", "sofia"))