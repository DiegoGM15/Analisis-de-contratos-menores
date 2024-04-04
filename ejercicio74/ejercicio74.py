import pandas as pd
import matplotlib.pyplot as plt
import ejercicio74_funciones

tabla = pd.read_csv('c:/nueva/ejercicio74/contratos-menores-madrid.csv', sep=';', decimal='.')

tabla['SECCION'] = tabla['SECCION'].astype(str)
tabla['TIPO DE CONTRATO'] = tabla['TIPO DE CONTRATO'].astype(str)
tabla['ANO'] = tabla['ANO'].astype('int')
tabla['IMPORTE'] = tabla['IMPORTE'].astype(float)
tabla['CONTRATISTA'] = tabla['CONTRATISTA'].astype(str)
tabla['Identificador'] = tabla.groupby('SECCION').ngroup()

empresa_id = {seccion: i for i, seccion in enumerate(tabla['SECCION'].unique())}

tabla['ID SECCION'] = tabla['SECCION'].map(empresa_id)
tabla['ID SECCION'] = tabla['ID SECCION'].astype(int)

id_secciones = tabla['ID SECCION'].unique().tolist()
secciones = tabla['SECCION'].unique().tolist()
empresas = tabla['CONTRATISTA'].unique().tolist()
aniomin = tabla['ANO'].min()
aniomax = tabla['ANO'].max()

""" for seccion in secciones:

        nombre_seccion = tabla.loc[tabla['ID SECCION'] == seccion, 'SECCION']

print(nombre_seccion) """

testigo1 = False
testigo2 = False
testigo3 = False

while (testigo1 == False):

    print(empresas)
    empresa = input("Introduce el nombre de la empresa que quieras buscar: ") 

    if empresa in empresas:

        print('La empresa esta en la lista')
        testigo1 = True

    else:

        print('La empresa no esta en la lista de empresas')
        testigo1 = False
menor = ''
mayor = ''

while(testigo2 == False):

    try: 
        anio1 = int(input(f'Introduce un año entre {aniomin}-{aniomax}: '))
        anio2 = int(input(f'Introduce otro año distinto al anterior entre {aniomin}-{aniomax}: '))

        if (anio1 < aniomin or anio2 > aniomax or anio2 < aniomin or anio1 > aniomax):
            
            print('Los años estan mal')
            testigo2 = False
            
        elif(anio1 < anio2):

            mayor = anio2
            menor = anio1
            print('Los años estan bien')
            testigo2 = True

        else:
            mayor = anio1
            menor = anio2
            print("Los años estan bien")
            testigo2= True

    except ValueError:
        print("Las fechas no son correctas. Repíte las fechas.")

while(testigo3 == False):

    try:

        print(id_secciones)
        seccion = int(input('Introduce un ID de seccion: '))

        if seccion in id_secciones:
            
            print('La seccion está en la lista')
            testigo3 = True

        else: 

            print('La seccion no está en la lista')
            testigo3= False

    except ValueError:
        print("Los datos introducidos están mal")

lista_4secciones = []

while (len(lista_4secciones) < 4):

    testigo = False

    while (testigo == False):

        cod_seccion = int(input('Introduce un codigo de seccion: '))

        if cod_seccion in id_secciones:

            testigo = True

            if cod_seccion in lista_4secciones:

                print ("Ese código de sección está repetido, escribe otro.")

            else:

                lista_4secciones.append(cod_seccion)
                
        else: 
                
            print('Ese código de sección no está en la tabla, repitelo.')


resultado = ejercicio74_funciones.total_facturado_seccion(tabla,menor,mayor,seccion)
resultado1 = ejercicio74_funciones.total_facturado_empresa(tabla, menor,mayor,empresa)
resultado2 = ejercicio74_funciones.facturado_empresa_seccion(tabla,menor,mayor,empresa,seccion)
resultado3 = ejercicio74_funciones.empresas_facturado(tabla,menor,mayor,10)
resultado4 = ejercicio74_funciones.total_facturado_grafico(tabla,menor,mayor,10)
resultado5 = ejercicio74_funciones.anual_secciones(tabla,menor,mayor,lista_4secciones)