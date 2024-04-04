import pandas as pd
import matplotlib.pyplot as plt

def total_facturado_seccion(dataframe,anio1, anio2, id_seccion): #Crear una función que reciba una sección y una lista de años y devuelva un diccionario con el número de contratos y el total facturado a la sección esos años.

    filtro = (dataframe['ID SECCION'] == id_seccion) & (dataframe['ANO'] >= anio1) & (dataframe['ANO'] <= anio2)
    tabla_filtrada = dataframe.loc[filtro]

    tabla_total = tabla_filtrada.groupby(['SECCION','TIPO DE CONTRATO'])['IMPORTE'].sum()
    tabla_dic = tabla_total.to_dict()
    tabla_total.to_csv('c:/nueva/ejercicio74/total-facturado-seccion.csv', sep=';', decimal=',')

    return tabla_total

#resultado = total_facturado_seccion(tabla,2018,2019,0)

def total_facturado_empresa(dataframe,anio1, anio2,empresa): #Crear una función que reciba una empresa y una lista de años y devuelva un diccionario con el número de contratos y el total facturado por la empresa esos años.

    filtro = (dataframe['CONTRATISTA'] == empresa) & (dataframe['ANO'] >= anio1) & (dataframe['ANO'] <= anio2)
    tabla_filtrada = dataframe.loc[filtro]

    tabla_total = tabla_filtrada.groupby(['CONTRATISTA','TIPO DE CONTRATO'])['IMPORTE'].sum()
    tabla_total.to_csv('c:/nueva/ejercicio74/total-facturado-empresa.csv', sep=';', decimal=',')

    return tabla_total

#resultado1 = total_facturado_empresa(tabla, 2018,2019,'MORASA S.A.')

def facturado_empresa_seccion(dataframe,anio1,anio2,empresa,seccion):

    filtro = filtro = (dataframe['CONTRATISTA'] == empresa) & (dataframe['ANO'] >= anio1) & (dataframe['ANO'] <= anio2) & (dataframe['ID SECCION'] == seccion)
    tabla_filtrada = dataframe.loc[filtro]

    tabla_facturado = tabla_filtrada.groupby(['CONTRATISTA','SECCION','TIPO DE CONTRATO'])['IMPORTE'].sum()
    tabla_facturado.to_csv('c:/nueva/ejercicio74/facturado-empresas-seccion.csv', sep=';', decimal=',')

    return tabla_facturado

#resultado2 = facturado_empresa_seccion(tabla, 2017,2019,'AGENCIA EVOL  PUBLICIDAD, S.A.',4)

def empresas_facturado(dataframe,anio1,anio2,nentero):

    filtro = (dataframe['ANO'] >= anio1) & (dataframe['ANO'] <= anio2)
    tabla_filtrada = dataframe.loc[filtro]
    tabla_agrupada = tabla_filtrada.groupby(['CONTRATISTA'])['IMPORTE'].sum().sort_values(ascending=False)
    top_empresas = tabla_agrupada.nlargest(nentero)
    plt.figure(figsize=(12, 6))
    top_empresas.plot(kind='bar', color='skyblue')
    plt.title(f'Top {nentero} empresas con mayor facturacion entre los años {anio1}-{anio2}')
    plt.xlabel('EMPRESAS')
    plt.ylabel('FACTURACION')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    #plt.subplots_adjust(bottom=0.3, top=0.9)
    plt.savefig('c:/nueva/ejercicio74/empresas_facturado.png')
    plt.show()

#resultado3 = empresas_facturado(tabla,2017,2019,10)

def total_facturado_grafico(dataframe,anio1,anio2,nentero):

    filtro = (dataframe['ANO'] >= anio1) & (dataframe['ANO'] <= anio2)
    tabla_filtrada = dataframe.loc[filtro]

    tabla_agrupado = tabla_filtrada.groupby(['ANO', 'CONTRATISTA'])['IMPORTE'].sum().reset_index()
    top_empresas = tabla_agrupado.groupby('CONTRATISTA')['IMPORTE'].sum().nlargest(nentero)
    empresas = pd.Series(top_empresas.index, index=top_empresas.values)
    
    for empresa in empresas.values:

        tabla_empresas = tabla_agrupado[tabla_agrupado['CONTRATISTA'] == empresa]
        plt.plot(tabla_empresas['ANO'], tabla_empresas['IMPORTE'], label = empresa)
        
    plt.title(f'Evolucion anual del total facturado por las {nentero} empresas que mas han facturado')
    plt.xlabel('AÑO')
    plt.ylabel('FACTURACION')
    plt.xticks(rotation=90)
    plt.legend(title='Empresas',loc='best')
    plt.grid(True)
    plt.tight_layout()
    #plt.subplots_adjust(bottom=0.3, top=0.9)
    plt.savefig('c:/nueva/ejercicio74/evaluacionanual_facturado.png')
    plt.show()

    #return empresas

#resultado4 = total_facturado_grafico(tabla,2000,2019,10)
#print(resultado1)                               
#print(resultado)
#print(resultado3)
#print(resultado4)

def anual_secciones(dataframe,anio1,anio2,secciones):

    filtro = dataframe[(dataframe['ANO'] >= anio1) & (dataframe['ANO'] <= anio2) & (dataframe['ID SECCION'].isin(secciones))]
    facturado_secciones = filtro.groupby(['ANO','SECCION','ID SECCION'])['IMPORTE'].sum().reset_index()

    #return facturado_secciones
    for seccion in secciones:

        nombre_seccion = facturado_secciones.loc[facturado_secciones['ID SECCION'] == seccion, 'SECCION'].iloc[0]
        datos=facturado_secciones[facturado_secciones['ID SECCION'] == seccion]
        plt.plot(datos['ANO'],datos['IMPORTE'], label=nombre_seccion)

    plt.xlabel('Año')
    plt.ylabel('Importe')
    plt.title(f'Evolución anual de las secciones entre los años {anio1} y {anio2}')
    plt.legend(title='Secciones', fontsize='small',loc='best')
    plt.xticks(range(anio1,anio2+1),rotation=90)
    plt.tight_layout()
    plt.savefig("C:/nueva/ejercicio74/anual_secciones.png")
    plt.show()

#resultado5 = anual_secciones(tabla,2000,2019,[0,1,2,3])
#print(resultado5)