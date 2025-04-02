#Importar una funcion de tabulate de la libreria de tabulate
from tabulate import tabulate
#Funcion en donde se llama menu, y se inicializa la lista_tareas
def inicio():
    lista_tarea=[]
    print('--------------------------Bienvenido--------------------------')
    menu(lista_tarea)
#funcion en donde termina el programa
def terminar():
    print('--------------------------End--------------------------')
#Funcion en
def menu(lista_tarea):
    print('--------------------------Menu--------------------------')
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
    
def agregar_tarea(lista_tarea):
    tamano=len(lista_tarea)
    print('--------------------------Agregar tarea--------------------------')
    titulo=input('Ingrese el titulo de la tareas: ')
    descripcion=input('Ingrese la descripcion de la tarea: ')
    estado='Pendiente'
    lista_tarea.append([tamano+1,titulo,descripcion,estado])
    print('-----------------------------------------------------------------')
    print('1. Agregar otra tarea\n2. Ir a menu')
    opcion=int(input('Ingrese la opcion que desea: '))
    if opcion==1:
        agregar_tarea(lista_tarea)
    return lista_tarea
def ver_tareas(lista_tareas):
    tamano=len(lista_tareas)
    print('-------------------Lista de tareas---------------------------')
    print(f"id      Titulo                        Descripcion                           Estado")
    for i in range(tamano):
        id=lista_tareas[i][0]
        titulo=lista_tareas[i][1]
        descripcion=lista_tareas[i][2]
        estado="Completado" if lista_tareas[i][3]==1 else "Pendiente" 
        print(f"{i+1}     {titulo}        {descripcion}      {estado}")
    print(tabulate(lista_tareas,headers=['Id','Titulo','Descripcion','Estado'],tablefmt="grid"))
def eliminar_tarea(lista_tareas):
    ver_tareas(lista_tareas)
    print('---------------------Eliminar tarea--------------------------')
    lista_borrar=int(input('Ingresa el id de la tarea que deseas borrar '))-1
    #Agregar estar seguro de borrar esta lista
    if lista_borrar<len(lista_tareas) and lista_borrar>-1:
        lista_tareas.pop(lista_borrar)
    else:
        print('Ingrese un valor valido')
        eliminar_tarea(lista_tareas)
    return lista_tareas
def marcar_completada(lista_tareas):
    ver_tareas(lista_tareas)
    print('--------------------------Marcar completada tarea--------------------------')
    tarea_cambio_estado=int(input('Ingresa el id de la tarea que deseas cambiar el estado a Completado '))-1
    if tarea_cambio_estado < len(lista_tareas) and tarea_cambio_estado>-1:
        lista_tareas[tarea_cambio_estado][3]='Completado'
    else:
        print('Ingrese un valor valido')
        marcar_completada(lista_tareas)
    ver_tareas(lista_tareas)
    return lista_tareas
inicio()