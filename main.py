def inicio():
    lista_tarea=[]
    print('--------------Bienvenido-----------------')
    menu(lista_tarea)
def terminar():
    print('-----------------End--------------------')
def menu(lista_tarea):
    print('----------------Menu---------------------')
    print('\n1. Agregar tarea nueva\n2. Eliminar tarea\n3. Ver tarea\n4. Marcar como completada una tarea\n0. Salir')
    opcion=int(input('Seleccione la opcion que desea: '))
    if opcion==1:
        lista_tarea=agregar_tarea(lista_tarea)
        menu(lista_tarea)
    elif opcion==2:
        lista_tarea=eliminar_tarea(lista_tarea)
        menu(lista_tarea)
    elif opcion==3:
        ver_tareas(lista_tarea)
        menu(lista_tarea)
    elif opcion==4:
        lista_tarea=marcar_completada(lista_tarea)
        menu(lista_tarea)
    elif opcion==0:
        terminar()
    else:
        print('Opcion incorrecta. Eliga nuevamente una opcion valida')
        menu(lista_tarea)
    
def agregar_tarea(lista_tarea): # type: ignore
    print('--------------Agregar tarea---------------------')
    titulo=input('Ingrese el titulo de la tareas: ')
    descripcion=input('Ingrese la descripcion de la tarea: ')
    estado=0
    lista_tarea.append([titulo,descripcion,estado])
    print('------------------------------------------------')
    print('1. Agregar otra tarea\n2. Ir a menu')
    opcion=int(input('Ingrese la opcion que desea: '))
    if opcion==1:
        agregar_tarea(lista_tarea)
    return lista_tarea
def ver_tareas(lista_tareas):
    tamano=len(lista_tareas)
    print('-------------------Lista de tareas---------------------------')
    print(f"id      Titulo                      Descripcion                     Estado")
    for i in range(tamano):
        titulo=lista_tareas[i][0]
        descripcion=lista_tareas[i][1]
        estado="Completado" if lista_tareas[i][2]==1 else "Pendiente" 
        print(f"{i+1}     {titulo}        {descripcion}      {estado}")
    
def eliminar_tarea(lista_tareas):
    ver_tareas(lista_tareas)
    print('---------------------Eliminar tarea--------------------------')
    lista_borrar=int(input('Ingresa el id de la tarea que deseas borrar '))-1
    #Agregar estar seguro de borrar esta lista
    lista_tareas.pop(lista_borrar)
    print(lista_tareas)
    return lista_tareas
def marcar_completada(lista_tareas):
    ver_tareas(lista_tareas)
    print('-----------------Marcar compleatda tarea---------------------')
    tarea_cambio_estado=int(input('Ingresa el id de la tarea que deseas cambiar el estado a Completado '))-1
    lista_tareas[tarea_cambio_estado][2]=1
    ver_tareas(lista_tareas)
    return lista_tareas
inicio()