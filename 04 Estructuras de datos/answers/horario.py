

def registrar_asignatura(horario, dia, asignatura):

    for dia_horario, asignaturas_horario in horario.items():
        if dia == dia_horario:
            # evita asignaturas repetidas en un día
            if asignatura not in asignaturas_horario:
                horario[dia_horario].append(asignatura)

    return


def dias_con_clase(horario, asignatura):
    dias = []
    for dia, asignaturas in horario.items():
        if asignatura in asignaturas:
            dias.append(dia)

    return dias

horario = {
    'Lunes': ['Cálculo I', 'Algebra I', 'Geometría y Trigonometría'],
    'Martes': ['Algebra I', 'Topográfia I'],
    'Miercoles': ['Cálculo I', 'Algebra I'],
    'Jueves': ['Topografía I'],
    'Viernes': ['Geometría y Trigonometría', 'Topografía']
}

registrar_asignatura(horario, 'Lunes', 'Cálculo II')

