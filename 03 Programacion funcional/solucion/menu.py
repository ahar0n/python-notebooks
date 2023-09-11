def mi_menu(opciones):
    print('Menú')
    opciones_list = []
    for opcion, descripcion in opciones:
        opciones_list.append(opcion)
        print('{}. {}'.format(opcion, descripcion))
    while True:
        entrada = input('Ingrese una opción: ')
        if entrada in opciones_list:
            break
    print('Ha elegido la opción {}'.format(entrada))

mis_opciones = [
    ('1', 'Buscar'),('2', 'Guardar como'), ('3', 'Editar'), ('4', 'Cerrar')
]
mi_menu(mis_opciones)