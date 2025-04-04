#Sistema de puntuacion:
puntos_kills = 3
puntos_asistencia = 1
puntos_deaths = -1


def calcular_puntaje(kills, assists, deaths):
    puntos = (kills*puntos_kills)+(assists*puntos_asistencia)
    if deaths:
        puntos+=puntos_deaths
    return puntos

