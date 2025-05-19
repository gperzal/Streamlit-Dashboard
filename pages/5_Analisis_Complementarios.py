import streamlit as st
import plotly.express as px
from utils.preprocessing import load_data, filter_data

st.set_page_config(page_title="📌 Análisis Complementarios", layout="wide")
st.title("📌 Análisis Complementarios y Exploración Específica")

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
    "⭐ Distribución de Calificaciones",
    "💳 Métodos de Pago Preferidos",
    "🧱 Ingreso Bruto por Sucursal y Producto"
])

# Tab 1 - Rating
with tabs[0]:
    st.subheader("⭐ Distribución de Calificaciones de Clientes")
    st.markdown("Se analiza cómo los clientes calificaron su experiencia en las tiendas.")
    if "Rating" in filtered_df.columns:
        fig = px.histogram(filtered_df, x="Rating", nbins=20, title="Distribución de Calificaciones")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("> 📌 **Interpretación**: Las calificaciones altas indican satisfacción general positiva. Permite monitorear la percepción del servicio.")
    else:
        st.warning("No se encontró la columna 'Rating'.")

# Tab 2 - Payment
with tabs[1]:
    st.subheader("💳 Métodos de Pago Preferidos")
    st.markdown("Análisis de frecuencia de los métodos de pago utilizados por los clientes.")
    if "Payment" in filtered_df.columns:
        payment_count = filtered_df["Payment"].value_counts().reset_index()
        payment_count.columns = ["Método", "Cantidad"]
        fig = px.bar(payment_count, x="Método", y="Cantidad", title="Frecuencia de Métodos de Pago")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("> 📌 **Interpretación**: Ayuda a detectar tendencias de medios de pago y planificar infraestructura (como POS, QR, etc).")
    else:
        st.warning("No se encontró la columna 'Payment'.")

# Tab 3 - Gross Income por Branch y Product line
with tabs[2]:
    st.subheader("🧱 Ingreso Bruto por Sucursal y Línea de Producto")
    st.markdown("Comparativa del ingreso bruto generado por combinación de tienda y línea de producto.")
    if "gross income" in filtered_df.columns and "Branch" in filtered_df.columns and category_col:
        pivot_df = filtered_df.groupby(["Branch", category_col])["gross income"].sum().reset_index()
        fig = px.sunburst(pivot_df, path=["Branch", category_col], values="gross income",
                          title="Composición de Ingreso Bruto por Sucursal y Línea de Producto")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("> 📌 **Interpretación**: Permite identificar combinaciones altamente rentables que pueden ser reforzadas estratégicamente.")
    else:
        st.warning("Faltan columnas para construir el gráfico.")