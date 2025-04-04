from src.__init__ import calcular_puntaje
from main import rounds

#Diccionario que almacena las estadisticas de los juadores
stats_jugadores = {}

for i, ronda in enumerate(rounds, 1):
    print(f"Ranking ronda {i}:")
    mvp = None
    max_puntos = -999

    for jugador, stats in ronda.items():
        kills = stats['kills'] 
        assists = stats['assists']
        deaths = stats ['deaths']
        puntos = calcular_puntaje(kills, assists, deaths)

        stats_jugadores[jugador]['kills']+=kills
        stats_jugadores[jugador]['assists']+=assists
        if deaths:
            stats_jugadores[jugador]['deaths']+=1
        stats_jugadores[jugador]['puntos']+=puntos

        if puntos>max_puntos:
            max_puntos = puntos
            mvp = jugador
    stats_jugadores[mvp]['mvp']+=1

    #Ordeno a los jugadores por puntaje obtenido
    ranking = sorted(stats_jugadores.items(), key=lambda x: x[1]['puntos'], reverse=True)

    #Imprimo el ranking de la ronda anctual
    print("Jugador    Kills  Asistencias  Muertes  MVPs  Puntos")
    print("-" * 50)
    for jugador, stats in ranking:
        print(f"{jugador:<10} {stats['kills']:<5} {stats['assists']:<10} {stats['deaths']:<7} {stats['mvps']:<5} {stats['puntos']:<5}")
    print("=" * 50)


