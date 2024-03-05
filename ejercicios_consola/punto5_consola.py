while True:
    respuesta = input('¿Desea continuar Si/No? ')
    
    if respuesta.lower() == 'no':
        break  # Salir del bucle si la respuesta es 'No'
    elif respuesta.lower() == 'si':
        # Aquí puedes poner el código que deseas ejecutar si la respuesta es 'Si'
        print('Continuando...')
    else:
        print('Respuesta no válida. Por favor, ingrese Si o No.')
