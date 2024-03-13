import pandas as pd

notes = [1, 6, 8, 9, 10, 6, 5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]

notas_arregladas = []
noms_complets = []
notes_textuals = []
llista_final = []  # Definimos la lista llista_final aquí

#para que las notas del for siguiente se guarden en una lista, se ha de crear una
notas_arregladas = []

noms_complets=[]

notes_textuals=[]

# para sumar un punto a cada nota, pero a la vez, asegurarse de que la nota máxima no supere 10
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
