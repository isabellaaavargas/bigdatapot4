import pandas as pd

# Leer el archivo Excel
df = pd.read_excel("KEXP.xlsx")

# Calcular el promedio de espectadores, comentarios y likes del canal
promedio_espectadores = df["viewCount"].mean()
promedio_comentarios = df["commentCount"].mean()
promedio_likes = df["likeCount"].mean()

df["desviacion_abs_espectadores"] = df["viewCount"] - promedio_espectadores
df["desviacion_abs_comentarios"] = df["commentCount"] - promedio_comentarios
df["desviacion_abs_likes"] = df["likeCount"] - promedio_likes

df["desviacion_pct_espectadores"] = (df["desviacion_abs_espectadores"] / promedio_espectadores) * 100
df["desviacion_pct_comentarios"] = (df["desviacion_abs_comentarios"] / promedio_comentarios) * 100
df["desviacion_pct_likes"] = (df["desviacion_abs_likes"] / promedio_likes) * 100

df = df.drop(["channelId", "categoryId","channelTitle", "tags","publishedAt","blacked_at"], axis=1)


# Guardar el DataFrame en un nuevo archivo Excel
df.to_excel("nom_dataset.xlsx", index=False)

index = df["viewCount"].idmax()
print(df.iloc[index])
