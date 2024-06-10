import pandas as pd

#Los datos iniciales

notes = [1, 6, 8, 9, 10, 6, 5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]


# Se han de crear listas para almacenar resultados del for siguiente

notas_arregladas = [] #Esta lista almacena las notas luego de ajustarlas
noms_complets = [] #Esta lista almacena los nombres completos
notes_textuals = [] #Esta lista almacena las calificaciones en texto
llista_final = []  # Definimos la lista llista_final aquí para almacenar los datos finales de cada alumno


# para sumar un punto a cada nota, pero a la vez, asegurarse de que la nota máxima no supere 10, se almacena en notas_arregladas

for nota in notes:
    if nota < 10:
        nota = nota+1
        notas_arregladas.append(nota)
    else:
        notas_arregladas.append(nota)


# Generamos los nombres completos y los almacenamos en noms_complets

for nom, cognom in zip(alumnes, cognoms):
    nom_complet = nom + " " + cognom
    noms_complets.append(nom_complet)


# Conversión de notas numéricas a calificaciones textuales y almacenamiento en notes_textuals

for n in notas_arregladas:
    if n == 10:
        valor = "matrícula de honor"
        notes_textuals.append(valor)
    elif n < 5:
        valor = "suspendido"
        notes_textuals.append(valor)
    elif n >= 5 and n <= 6:
        valor = "aprobado"
        notes_textuals.append(valor)
    elif n > 6 and n < 7:
        valor = "bien"
        notes_textuals.append(valor)
    elif n >= 7 and n <9:
        valor = "notable"
        notes_textuals.append(valor)
    else:
        valor = "Excelente"
        notes_textuals.append(valor)


# Construimos un diccionario con los datos de cada alumno y lo agregamos a la lista llista_final

for n, nom, q in zip(notas_arregladas, noms_complets, notes_textuals):
    dades = {"nom_alumne": nom, "nota": n, "qualificacio": q}
    llista_final.append(dades)


# Creamos el DataFrame utilizando la lista llista_final

df = pd.DataFrame(llista_final)
print(df)

# Guardamos el DataFrame como un archivo CSV

df.to_csv("dades.csv", index=False)
