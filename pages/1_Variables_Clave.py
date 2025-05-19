import streamlit as st
import plotly.express as px
from utils.preprocessing import load_data, filter_data

st.set_page_config(page_title="📌 Variables Clave", layout="wide")
st.title("📌 Selección y Análisis de Variables Clave")

# Cargar datos
df = load_data()

# Sidebar inputs
category_col = next((col for col in ["Category", "Product line"] if col in df.columns), None)
categorias = df[category_col].unique() if category_col else []
branches = df["Branch"].unique() if "Branch" in df.columns else []

start_date = st.sidebar.date_input("📅 Fecha inicio", df["Date"].min())
end_date = st.sidebar.date_input("📅 Fecha fin", df["Date"].max())
selected_categories = st.sidebar.multiselect("🏷️ Categorías", categorias, default=categorias)
selected_branches = st.sidebar.multiselect("🏬 Sucursales", branches, default=branches)

filtered_df = filter_data(df, start_date, end_date, selected_categories, category_col, selected_branches)

# KPIs principales
st.markdown("## 📈 Indicadores Clave del Segmento Actual")
col1, col2, col3 = st.columns(3)
col1.metric("🧾 Transacciones", len(filtered_df))
col2.metric("💰 Ventas Totales", f"${filtered_df['Total'].sum():,.2f}")
col3.metric("🧮 Promedio por Venta", f"${filtered_df['Total'].mean():,.2f}")

# Tabs para exploración
tabs = st.tabs(["👁 Vista Previa", "📊 Estadísticas", "📋 Análisis Visual", "🧠 Justificación"])

# Tab 1 - Vista previa
with tabs[0]:
    st.subheader("👁 Primeros registros filtrados")
    df_display = filtered_df.copy()
    if "Date" in df_display.columns:
        df_display["Date"] = df_display["Date"].astype(str)
    st.dataframe(df_display.head())

# Tab 2 - Estadísticas
with tabs[1]:
    st.subheader("📊 Resumen estadístico de variables numéricas")
    stats = filtered_df.select_dtypes(include='number').describe()
    st.dataframe(stats)

# Tab 3 - Análisis Visual
with tabs[2]:
    st.subheader("📋 Visualización rápida de variables clave")

    if "Date" in filtered_df.columns and "Total" in filtered_df.columns:
        st.markdown("#### 📆 Evolución Temporal de Ventas")
        df_time = filtered_df.groupby("Date")["Total"].sum().reset_index()
        fig_time = px.line(df_time, x="Date", y="Total", title="Ventas Totales a lo Largo del Tiempo")
        st.plotly_chart(fig_time, use_container_width=True)

    if "Branch" in filtered_df.columns:
        st.markdown("#### 🏪 Ventas por Sucursal")
        fig_branch = px.bar(filtered_df.groupby("Branch")["Total"].sum().reset_index(), 
                            x="Branch", y="Total", title="Total de Ventas por Sucursal")
        st.plotly_chart(fig_branch, use_container_width=True)

    if category_col:
        st.markdown("#### 🧺 Participación por Categoría")
        fig_cat = px.pie(filtered_df, names=category_col, values="Total", title="Distribución por Categoría")
        st.plotly_chart(fig_cat, use_container_width=True)

# Tab 4 - Justificación
with tabs[3]:
    st.subheader("🧠 Justificación de variables clave")
    st.markdown(f"""
Las siguientes variables han sido seleccionadas como clave en este análisis:

- **Total**: Representa el monto total por transacción, fundamental para evaluar ingresos.
- **Quantity**: Cantidad de productos por venta, útil para entender volumen de consumo.
- **Date**: Permite evaluar patrones temporales y estacionalidad.
- **Branch**: Compara desempeño entre tiendas.
- **Gender**: Permite entender el perfil demográfico de clientes.
- **{category_col or 'otra variable'}**: Da contexto sobre el tipo de producto o servicio adquirido.

> Estas variables son críticas para entender el rendimiento de ventas, ajustar campañas de marketing, optimizar stock, e incluso rediseñar el layout de tienda o catálogo.
""")
