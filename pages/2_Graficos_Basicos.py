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
tabs = st.tabs(["📈 Histograma de Ventas", "📦 Boxplot por Género", "🔍 Dispersión Total vs Cantidad"])

# Tab 1 - Histograma
with tabs[0]:
    st.subheader("📈 Distribución de Ventas Totales")
    st.markdown("Este gráfico permite observar cómo se distribuyen las ventas individuales en el período seleccionado.")
    if "Total" in filtered_df.columns:
        fig = px.histogram(filtered_df, x="Total", nbins=30, title="Distribución de Montos Totales de Venta")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No se encontró la columna 'Total' en el dataset.")

# Tab 2 - Boxplot
with tabs[1]:
    st.subheader("📦 Comparación de Ventas por Género")
    st.markdown("Este boxplot permite comparar los montos de venta promedio y su variabilidad entre géneros.")
    if "Gender" in filtered_df.columns and "Total" in filtered_df.columns:
        fig2 = px.box(filtered_df, x="Gender", y="Total", title="Distribución de Ventas por Género")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("Faltan columnas 'Gender' o 'Total'.")

# Tab 3 - Dispersión
with tabs[2]:
    st.subheader("🔍 Relación entre Cantidad y Total Vendido")
    st.markdown("Este gráfico revela si los clientes que compran más productos tienden a gastar más.")
    if "Quantity" in filtered_df.columns and "Total" in filtered_df.columns:
        fig3 = px.scatter(filtered_df, x="Quantity", y="Total", color="Gender" if "Gender" in filtered_df.columns else None,
                          title="Relación entre Cantidad de Productos y Monto Total")
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.warning("Faltan columnas 'Quantity' o 'Total'.")
