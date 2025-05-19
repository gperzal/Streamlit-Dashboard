import streamlit as st
import plotly.express as px
import pandas as pd
from utils.preprocessing import load_data, filter_data

st.set_page_config(page_title="📈 Gráficos Compuestos", layout="wide")
st.title("📈 Análisis Comparativo de Ventas")

# Cargar datos
df = load_data()

category_col = next((col for col in ["Category", "Product line"] if col in df.columns), None)
categorias = df[category_col].unique() if category_col else []
branches = df["Branch"].unique() if "Branch" in df.columns else []

start_date = st.sidebar.date_input("📅 Fecha inicio", df["Date"].min())
end_date = st.sidebar.date_input("📅 Fecha fin", df["Date"].max())
selected_categories = st.sidebar.multiselect("🏷️ Categorías", categorias, default=categorias)
selected_branches = st.sidebar.multiselect("🏬 Sucursales", branches, default=branches)

filtered_df = filter_data(df, start_date, end_date, selected_categories, category_col, selected_branches)

tabs = st.tabs([
    "📊 Tendencia por Categoría",
    "🏬 Ventas por Sucursal",
    "🔥 Sucursal vs Categoría",
    "📉 Costo vs Ganancia Bruta"
])

# Tab 1 - Línea temporal por categoría
with tabs[0]:
    st.subheader("📊 Evolución de Ventas por Categoría")
    st.markdown("Este gráfico permite observar cómo han variado las ventas (`Total`) para cada categoría a lo largo del tiempo.")

    if category_col and "Date" in filtered_df.columns and "Total" in filtered_df.columns:
        fig_line = px.line(filtered_df, x="Date", y="Total", color=category_col, title="Tendencia de Ventas por Categoría")
        st.plotly_chart(fig_line, use_container_width=True)

        st.markdown("""
        > 📌 **Interpretación**: Este análisis permite detectar estacionalidades o cambios de comportamiento por línea de producto. 
        Si una categoría crece de forma constante, podría ser priorizada en campañas o stock.
        """)
    else:
        st.warning("No se encontraron las columnas necesarias para generar la gráfica.")

# Tab 2 - Barras por sucursal
with tabs[1]:
    st.subheader("🏬 Comparación de Ventas por Sucursal")
    st.markdown("Visualización acumulada para entender qué tiendas han generado más ingresos en el período.")

    if "Branch" in filtered_df.columns and "Total" in filtered_df.columns:
        resumen_branch = filtered_df.groupby("Branch")["Total"].sum().reset_index()
        fig_bar = px.bar(resumen_branch, x="Branch", y="Total", title="Ventas Totales por Sucursal")
        st.plotly_chart(fig_bar, use_container_width=True)

        st.markdown("""
        > 📌 **Interpretación**: Este gráfico permite identificar cuál sucursal genera mayores ingresos y si hay alguna rezagada. 
        Es útil para enfocar esfuerzos operativos y de marketing.
        """)

# Tab 3 - Mapa de calor cruzado con gross income
with tabs[2]:
    st.subheader("🔥 Matriz de Rendimiento por Sucursal y Categoría (Ingreso Bruto)")
    st.markdown("Visualiza qué combinaciones de sucursal y categoría generan mayor `gross income`.")

    if category_col and "Branch" in filtered_df.columns and "gross income" in filtered_df.columns:
        pivot_df = pd.pivot_table(filtered_df, values="gross income", index="Branch", columns=category_col, aggfunc="sum", fill_value=0)
        fig_heatmap = px.imshow(pivot_df, text_auto=True, aspect="auto", color_continuous_scale="Oranges",
                                title="Ingreso Bruto por Sucursal y Categoría")
        st.plotly_chart(fig_heatmap, use_container_width=True)

        st.markdown("""
        > 📌 **Interpretación**: Ayuda a entender qué combinaciones generan más ganancia. Las celdas más oscuras indican mayor rentabilidad.
        Permite tomar decisiones de inventario y foco comercial por sucursal.
        """)
    else:
        st.warning("Faltan columnas necesarias para construir el mapa de calor.")

# Tab 4 - Scatter cogs vs gross income
with tabs[3]:
    st.subheader("📉 Relación entre Costo y Ganancia Bruta")
    st.markdown("Se analiza la relación entre `cogs` (costos) y `gross income` (ganancia bruta) para cada transacción.")

    if "cogs" in filtered_df.columns and "gross income" in filtered_df.columns:
        fig_scatter = px.scatter(filtered_df, x="cogs", y="gross income", color="Branch" if "Branch" in filtered_df.columns else None,
                                 trendline="ols", title="Costo vs Ganancia Bruta")
        st.plotly_chart(fig_scatter, use_container_width=True)

        st.markdown("""
        > 📌 **Interpretación**: Se observa una correlación positiva natural (a mayor costo, mayor ganancia), pero también permite detectar outliers o puntos ineficientes.
        La línea de tendencia ayuda a ver el comportamiento promedio.
        """)
    else:
        st.warning("Las columnas 'cogs' y/o 'gross income' no están disponibles en el conjunto de datos.")

