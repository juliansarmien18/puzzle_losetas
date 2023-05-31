from solucionador_losetas import SolucionadorLosetas
if __name__=='__main__':

    estado_inicial = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
    estado_objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    solucionador = SolucionadorLosetas(estado_inicial, estado_objetivo)
    solucion = solucionador.resolver_ramificacion_poda()

    if solucion is not None:
        print("Solución encontrada:", solucion)
    else:
        print("No se encontró solución.")