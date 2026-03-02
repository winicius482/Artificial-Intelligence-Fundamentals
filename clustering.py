import pandas as pd
from sklearn.cluster import KMeans

def aplicar_kmeans(arquivo, n_clusters=2):
    df = pd.read_csv(arquivo)
    if 'x' not in df.columns or 'y' not in df.columns:
        raise ValueError("O arquivo deve conter as colunas 'x' e 'y'")
    coords = df[['x','y']]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(coords)
    return df