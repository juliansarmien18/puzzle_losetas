class SolucionadorLosetas:
    def __init__(self, estado_inicial, estado_objetivo):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo

    def resolver_ramificacion_poda(self):
        nodos_abiertos = [(self.estado_inicial, [])]

        while nodos_abiertos:
            estado_actual, movimientos = nodos_abiertos.pop(0)
            
            if estado_actual == self.estado_objetivo:
                return movimientos

            movimientos_validos = self.obtener_movimientos_validos(estado_actual)

            for movimiento in movimientos_validos:
                nuevo_estado = self.aplicar_movimiento(estado_actual, movimiento)
                nuevos_movimientos = movimientos + [movimiento]
                nodos_abiertos.append((nuevo_estado, nuevos_movimientos))

    def obtener_movimientos_validos(self, estado):
        movimientos = []
        fila_vacia, columna_vacia = self.encontrar_posicion_vacia(estado)

        if fila_vacia > 0:
            movimientos.append('Arriba')
        if fila_vacia < len(estado) - 1:
            movimientos.append('Abajo')
        if columna_vacia > 0:
            movimientos.append('Izquierda')
        if columna_vacia < len(estado[0]) - 1:
            movimientos.append('Derecha')

        return movimientos

    def encontrar_posicion_vacia(self, estado):
        for i in range(len(estado)):
            for j in range(len(estado[0])):
                if estado[i][j] == 0:
                    return i, j

    def aplicar_movimiento(self, estado, movimiento):
        fila_vacia, columna_vacia = self.encontrar_posicion_vacia(estado)
        nuevo_estado = [fila.copy() for fila in estado]

        if movimiento == 'Arriba':
            nuevo_estado[fila_vacia][columna_vacia] = estado[fila_vacia - 1][columna_vacia]
            nuevo_estado[fila_vacia - 1][columna_vacia] = 0
        elif movimiento == 'Abajo':
            nuevo_estado[fila_vacia][columna_vacia] = estado[fila_vacia + 1][columna_vacia]
            nuevo_estado[fila_vacia + 1][columna_vacia] = 0
        elif movimiento == 'Izquierda':
            nuevo_estado[fila_vacia][columna_vacia] = estado[fila_vacia][columna_vacia - 1]
            nuevo_estado[fila_vacia][columna_vacia - 1] = 0
        elif movimiento == 'Derecha':
            nuevo_estado[fila_vacia][columna_vacia] = estado[fila_vacia][columna_vacia + 1]
            nuevo_estado[fila_vacia][columna_vacia + 1] = 0

        return nuevo_estado


