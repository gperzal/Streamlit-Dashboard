import streamlit as st
import plotly.express as px
from utils.preprocessing import load_data, filter_data

st.set_page_config(page_title="📊 Gráficos Básicos", layout="wide")
st.title("📊 Exploración Visual Básica")

# Cargar datos
df = load_data()

# Sidebar
category_col = next((col for col in ["Category", "Product line"] if col in df.columns), None)
categorias = df[category_col].unique() if category_col else []
branches = df["Branch"].unique() if "Branch" in df.columns else []

start_date = st.sidebar.date_input("📅 Fecha inicio", df["Date"].min())
end_date = st.sidebar.date_input("📅 Fecha fin", df["Date"].max())
selected_categories = st.sidebar.multiselect("🏷️ Categorías", categorias, default=categorias)
selected_branches = st.sidebar.multiselect("🏬 Sucursales", branches, default=branches)

filtered_df = filter_data(df, start_date, end_date, selected_categories, category_col, selected_branches)

# Tabs de visualización
tabs = st.tabs([
    "📈 Histograma de Ventas", 
    "📦 Boxplot por Género", 
    "🔍 Dispersión Total vs Cantidad",
    "⭐ Calificación de Clientes", 
    "👥 Gasto por Tipo de Cliente"
])

# Tab 1 - Histograma de Total
with tabs[0]:
    st.subheader("📈 Distribución de Ventas Totales")
    st.markdown("Este gráfico permite observar cómo se distribuyen los montos totales de venta por transacción.")
    if "Total" in filtered_df.columns:
        fig = px.histogram(filtered_df, x="Total", nbins=30, title="Distribución de Montos Totales de Venta")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("Se observa una mayor concentración de ventas entre valores bajos, lo que sugiere tickets promedio pequeños en gran parte de las transacciones.")
    else:
        st.warning("No se encontró la columna 'Total' en el dataset.")

# Tab 2 - Boxplot por Género
with tabs[1]:
    st.subheader("📦 Comparación de Ventas por Género")
    st.markdown("Este boxplot compara los montos de venta entre hombres y mujeres, permitiendo ver su variabilidad.")
    if "Gender" in filtered_df.columns and "Total" in filtered_df.columns:
        fig2 = px.box(filtered_df, x="Gender", y="Total", title="Distribución de Ventas por Género")
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("Ambos géneros presentan una distribución similar en cuanto a ticket de compra, sin diferencias significativas.")
    else:
        st.warning("Faltan columnas 'Gender' o 'Total'.")

# Tab 3 - Dispersión Quantity vs Total
with tabs[2]:
    st.subheader("🔍 Relación entre Cantidad y Total Vendido")
    st.markdown("Se visualiza la correlación entre la cantidad de productos y el monto final por transacción.")
    if "Quantity" in filtered_df.columns and "Total" in filtered_df.columns:
        fig3 = px.scatter(
            filtered_df, x="Quantity", y="Total", 
            color="Gender" if "Gender" in filtered_df.columns else None,
            title="Relación entre Cantidad de Productos y Monto Total"
        )
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("Existe una relación directa: a mayor cantidad, mayor total, lo que valida el correcto registro de ventas.")
    else:
        st.warning("Faltan columnas 'Quantity' o 'Total'.")

# Tab 4 - Distribución de Rating
with tabs[3]:
    st.subheader("⭐ Distribución de Calificaciones de Clientes")
    st.markdown("El siguiente histograma muestra cómo los clientes valoraron su experiencia.")
    if "Rating" in filtered_df.columns:
        fig4 = px.histogram(filtered_df, x="Rating", nbins=20, title="Distribución de Calificación de Clientes")
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown("Las calificaciones tienden a concentrarse entre 6 y 9 puntos, indicando un alto grado de satisfacción.")
    else:
        st.warning("No se encontró la columna 'Rating'.")

# Tab 5 - Gasto por Tipo de Cliente
with tabs[4]:
    st.subheader("👥 Comparación del Gasto por Tipo de Cliente")
    st.markdown("Compara el comportamiento de gasto entre clientes regulares y miembros.")
    if "Customer type" in filtered_df.columns and "Total" in filtered_df.columns:
        fig5 = px.box(filtered_df, x="Customer type", y="Total", title="Distribución de Gasto por Tipo de Cliente")
        st.plotly_chart(fig5, use_container_width=True)
        st.markdown("Ambos grupos muestran un comportamiento de gasto similar, aunque los miembros parecen tener una ligera mayor dispersión.")
    else:
        st.warning("Faltan columnas 'Customer type' o 'Total'.")
