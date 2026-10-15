import os

from src.experimentos import ESCENARIOS, ejecutar_escenario, tabla_comparativa
from src.graficas import graficar_cola, graficar_comparacion, graficar_esperas
from src.teoria import es_estable


def main():
    os.makedirs("resultados", exist_ok=True)
    resultados = []

    for esc in ESCENARIOS:
        n = esc["escenario"]
        lam = esc["lam"]
        mu = esc["mu"]

        if not es_estable(lam, mu):
            print(f"Escenario {n}: no estable")
            continue

        r = ejecutar_escenario(lam, mu)
        r["escenario"] = n
        resultados.append(r)

        titulo = f"Escenario {n} (lam={lam}, mu={mu})"
        graficar_cola(r["muestras_cola"], titulo, f"resultados/cola_esc{n}.png")
        graficar_esperas(r["tiempos_espera"], titulo, f"resultados/esperas_esc{n}.png")

    tabla_comparativa(resultados)
    graficar_comparacion(resultados, "resultados/comparacion.png")


if __name__ == "__main__":
    main()