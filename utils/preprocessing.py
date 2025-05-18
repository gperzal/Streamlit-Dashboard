
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(path: str = "data/data.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    return df

def filter_data(df: pd.DataFrame, start_date=None, end_date=None, categories=None, category_col=None, branches=None):
    filtered = df.copy()
    if "Date" in filtered.columns and start_date and end_date:
        filtered = filtered[(filtered["Date"] >= pd.to_datetime(start_date)) & (filtered["Date"] <= pd.to_datetime(end_date))]
    if category_col and categories:
        filtered = filtered[filtered[category_col].isin(categories)]
    if "Branch" in filtered.columns and branches:
        filtered = filtered[filtered["Branch"].isin(branches)]
    return filtered

def prepare_pca(df: pd.DataFrame, n_components=2):
    numeric = df.select_dtypes(include='number').dropna(axis=1)
    if numeric.shape[1] >= n_components:
        scaled = StandardScaler().fit_transform(numeric)
        return scaled, numeric
    return None, None
