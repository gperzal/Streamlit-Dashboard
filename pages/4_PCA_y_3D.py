
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from utils.preprocessing import load_data, filter_data, prepare_pca

st.set_page_config(page_title="🧬 Análisis Multivariado y 3D", layout="wide")
st.title("🧬 Análisis Multivariado Avanzado y Visualización 3D")

df = load_data()

category_col = next((col for col in ["Category", "Product line"] if col in df.columns), None)
categorias = df[category_col].unique() if category_col else []
branches = df["Branch"].unique() if "Branch" in df.columns else []

start_date = st.sidebar.date_input("📅 Fecha inicio", df["Date"].min())
end_date = st.sidebar.date_input("📅 Fecha fin", df["Date"].max())
selected_categories = st.sidebar.multiselect("🏷️ Categorías", categorias, default=categorias)
selected_branches = st.sidebar.multiselect("🏬 Sucursales", branches, default=branches)
n_clusters = st.sidebar.slider("🔢 Número de Clusters (KMeans)", min_value=2, max_value=6, value=3)

filtered_df = filter_data(df, start_date, end_date, selected_categories, category_col, selected_branches)
scaled, numeric = prepare_pca(filtered_df, n_components=3)

tabs = st.tabs(["🔄 Correlación", "📊 Scree Plot", "🧭 PCA 2D", "🌐 PCA 3D", "📌 Segmentos (Clusters)"])

# Tab 1 - Correlation heatmap
with tabs[0]:
    st.subheader("🔄 Correlación entre Variables Numéricas")
    if not numeric.empty:
        fig_corr, ax = plt.subplots()
        sns.heatmap(numeric.corr(), annot=True, fmt=".2f", cmap="Blues", ax=ax)
        st.pyplot(fig_corr)
    else:
        st.warning("No hay suficientes variables numéricas para calcular correlaciones.")

# Tab 2 - Scree Plot
with tabs[1]:
    st.subheader("📊 Varianza Explicada por Componentes (Scree Plot)")
    if scaled is not None:
        pca_expl = PCA(n_components=min(10, scaled.shape[1]))
        pca_expl.fit(scaled)
        exp_var = pca_expl.explained_variance_ratio_ * 100
        fig_scree = px.bar(x=[f"PC{i+1}" for i in range(len(exp_var))], y=exp_var,
                           labels={'x': 'Componentes', 'y': 'Varianza (%)'},
                           title="Porcentaje de Varianza Explicada por Componentes")
        st.plotly_chart(fig_scree, use_container_width=True)
    else:
        st.warning("No se pudo calcular la varianza explicada.")

# Tab 3 - PCA 2D
with tabs[2]:
    st.subheader("🧭 Análisis PCA en 2D")
    if scaled is not None:
        pca2 = PCA(n_components=2)
        components2 = pca2.fit_transform(scaled)
        pca_df = pd.DataFrame(components2, columns=["PCA1", "PCA2"])
        if category_col:
            pca_df[category_col] = filtered_df[category_col].values[:len(pca_df)]
        fig2d = px.scatter(pca_df, x="PCA1", y="PCA2", color=category_col,
                           title="Proyección PCA 2D por Categoría")
        st.plotly_chart(fig2d, use_container_width=True)
    else:
        st.warning("No hay suficientes columnas numéricas para aplicar PCA.")

# Tab 4 - PCA 3D
with tabs[3]:
    st.subheader("🌐 Visualización PCA en 3D")
    if scaled is not None:
        pca3 = PCA(n_components=3).fit_transform(scaled)
        pca3_df = pd.DataFrame(pca3, columns=["PC1", "PC2", "PC3"])
        if "Branch" in filtered_df.columns:
            pca3_df["Branch"] = filtered_df["Branch"].values[:len(pca3_df)]
        fig3d = px.scatter_3d(pca3_df, x="PC1", y="PC2", z="PC3", color="Branch",
                              title="Proyección 3D por Sucursal")
        st.plotly_chart(fig3d, use_container_width=True)
    else:
        st.warning("No hay suficientes datos para la visualización 3D.")

# Tab 5 - Clustering
with tabs[4]:
    st.subheader("📌 Segmentación con KMeans (Clustering)")
    if scaled is not None:
        kmeans = KMeans(n_clusters=n_clusters, n_init="auto", random_state=42).fit(scaled)
        clusters = kmeans.labels_
        pca2 = PCA(n_components=2)
        comp = pca2.fit_transform(scaled)
        cluster_df = pd.DataFrame(comp, columns=["PCA1", "PCA2"])
        cluster_df["Cluster"] = clusters
        fig_clusters = px.scatter(cluster_df, x="PCA1", y="PCA2", color=cluster_df["Cluster"].astype(str),
                                  title=f"Segmentación de Clientes/Tiendas en {n_clusters} Grupos")
        st.plotly_chart(fig_clusters, use_container_width=True)

        st.markdown("### 🧬 Descripción de Clusters (centroides normalizados)")
        centers = pd.DataFrame(kmeans.cluster_centers_, columns=numeric.columns)
        st.dataframe(centers.round(2))
    else:
        st.warning("No es posible aplicar clustering sin datos numéricos suficientes.")
