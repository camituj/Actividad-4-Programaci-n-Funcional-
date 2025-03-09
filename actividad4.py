import pandas as pd

def cargar_archivo(ruta, tipo):
    """Carga archivos CSV, XLSX, HTML o JSON en un DataFrame"""
    if tipo == "csv":
        return pd.read_csv(ruta)
    elif tipo == "xlsx":
        return pd.read_excel(ruta)
    elif tipo == "html":
        return pd.read_html(ruta)[0]
    elif tipo == "json":
        return pd.read_json(ruta)
    else:
        raise ValueError("Formato no soportado")

def rellenar_ffill(df):
    """Sustituye valores nulos con el método forward fill (ffill)"""
    return df.fillna(method='ffill')

def rellenar_bfill(df):
    """Sustituye valores nulos con el método backward fill (bfill)"""
    return df.fillna(method='bfill')

def rellenar_string(df, valor="Desconocido"):
    """Sustituye valores nulos con un string concreto"""
    return df.fillna(valor)

def rellenar_promedio(df):
    """Sustituye valores nulos con el promedio de la columna"""
    return df.fillna(df.mean(numeric_only=True))

def rellenar_mediana(df):
    """Sustituye valores nulos con la mediana de la columna"""
    return df.fillna(df.median(numeric_only=True))

def rellenar_constante(df, valor=0):
    """Sustituye valores nulos con una constante definida por el usuario"""
    return df.fillna(valor)

def identificar_nulos(df):
    """Identifica valores nulos por columna y en todo el dataframe"""
    return {
        "nulos_por_columna": df.isnull().sum(),
        "total_nulos": df.isnull().sum().sum()
    }
