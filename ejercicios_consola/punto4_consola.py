# Pedimos al usuario que seleccione un tipo de robot
tipo_robot = input('Seleccione un tipo de robot: Cilindrico (C), Cartesiano (A) o Esférico (E): ')

# Mostramos el tipo y número de articulaciones según el tipo de robot seleccionado
tipo_robot = tipo_robot.upper()  # Convertir a mayúsculas para hacer la comparación más flexible

if tipo_robot == 'C':
    print('Robot Cilindrico:')
    print('- Tipo: 3 revolutas.')
    print('- Número de articulaciones: 3.')
elif tipo_robot == 'A':
    print('Robot Cartesiano:')
    print('- Tipo: 3 lineales.')
    print('- Número de articulaciones: 3.')
elif tipo_robot == 'E':
    print('Robot Esférico:')
    print('- Tipo: 2 revolutas y 1 prismática.')
    print('- Número de articulaciones: 3.')
else:
    print('El tipo de robot seleccionado no es válido.')
