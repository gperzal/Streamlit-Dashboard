
import streamlit as st
import plotly.express as px
from utils.preprocessing import load_data, filter_data

st.set_page_config(page_title="📋 Resumen Ejecutivo", layout="wide")
st.title("📋 Resumen Ejecutivo de Ventas")

df = load_data()

category_col = next((col for col in ["Category", "Product line"] if col in df.columns), None)
categorias = df[category_col].unique() if category_col else []
branches = df["Branch"].unique() if "Branch" in df.columns else []

start_date = st.sidebar.date_input("📅 Fecha inicio", df["Date"].min())
end_date = st.sidebar.date_input("📅 Fecha fin", df["Date"].max())
selected_categories = st.sidebar.multiselect("🏷️ Categorías", categorias, default=categorias)
selected_branches = st.sidebar.multiselect("🏬 Sucursales", branches, default=branches)

filtered_df = filter_data(df, start_date, end_date, selected_categories, category_col, selected_branches)

tabs = st.tabs(["📊 Panel de Indicadores", "🧠 Análisis Automatizado"])

# TAB 1 - Visual
with tabs[0]:
    st.subheader("📊 Indicadores Clave del Período Seleccionado")

    if "Total" in filtered_df.columns:
        col1, col2, col3 = st.columns(3)
        col1.metric("🧾 Transacciones", len(filtered_df))
        col2.metric("💰 Ventas Totales", f"${filtered_df['Total'].sum():,.2f}")
        col3.metric("🧮 Promedio por Venta", f"${filtered_df['Total'].mean():,.2f}")

    if "Branch" in filtered_df.columns:
        st.markdown("### 🏪 Ventas Totales por Sucursal")
        resumen_branch = filtered_df.groupby("Branch")["Total"].sum().reset_index()
        fig_sucursal = px.bar(resumen_branch, x="Branch", y="Total", title="Ingresos por Sucursal")
        st.plotly_chart(fig_sucursal, use_container_width=True)

    if category_col and "Total" in filtered_df.columns:
        st.markdown("### 📦 Participación por Categoría de Producto")
        fig_categoria = px.pie(filtered_df, names=category_col, values="Total", title="Distribución de Ventas por Categoría")
        st.plotly_chart(fig_categoria, use_container_width=True)

# TAB 2 - Dinámico
with tabs[1]:
    st.subheader("🧠 Recomendaciones Gerenciales Automáticas")

    if "Branch" in filtered_df.columns and "Total" in filtered_df.columns:
        resumen_branch = filtered_df.groupby("Branch")["Total"].sum().reset_index()
        avg_ticket = filtered_df.groupby("Branch")["Total"].mean().reset_index()
        top_branch = resumen_branch.sort_values("Total", ascending=False).iloc[0]
        top_avg_ticket = avg_ticket.sort_values("Total", ascending=False).iloc[0]

        st.markdown(f"""
        ### 🏆 Sucursal Destacada
        - **{top_branch['Branch']}** es la sucursal con mayores ventas totales: **${top_branch['Total']:.2f}**
        - También destaca en ticket promedio: **${top_avg_ticket['Total']:.2f}**

        """)

        low_performing = resumen_branch.sort_values("Total").iloc[0]
        st.markdown(f"""
        ### ⚠️ Sucursal con Menor Rendimiento
        - **{low_performing['Branch']}** presenta el menor ingreso total: **${low_performing['Total']:.2f}**
        """)

    if category_col and "Total" in filtered_df.columns:
        cat_total = filtered_df.groupby(category_col)["Total"].sum().sort_values(ascending=False)
        dominant_cat = cat_total.index[0]
        dominant_pct = cat_total.iloc[0] / cat_total.sum()

        if dominant_pct > 0.5:
            st.warning(f"⚠️ La categoría **{dominant_cat}** representa el {dominant_pct:.0%} del total. Esto podría indicar una **dependencia excesiva** de este tipo de producto.")
        else:
            st.success(f"La categoría principal es **{dominant_cat}**, con una participación saludable del {dominant_pct:.0%}.")

        st.markdown("### 🔄 Distribución por Categoría")
        st.dataframe(cat_total.reset_index().rename(columns={"Total": "Total Vendido"}))

    st.markdown("## ✅ Recomendaciones de Mejora")
    st.markdown("""
1. Reforzar promoción en tiendas con menor rendimiento.
2. Diversificar categorías si existe dependencia alta.
3. Mantener impulso en tiendas y categorías líderes.
4. Realizar seguimiento mensual con este dashboard para detectar nuevas oportunidades.

Este panel genera hallazgos **directamente desde los datos**, facilitando la toma de decisiones en tiempo real.
""")
