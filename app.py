import streamlit as st

st.set_page_config(page_title="Dashboard Tiendas - Visión Gerencial", layout="wide")

# Encabezado principal
st.title("📊 Dashboard de Ventas - Visión Ejecutiva")
st.markdown("Bienvenido al centro de análisis estratégico de nuestra cadena de tiendas de conveniencia.")

# Imagen representativa
st.image("https://miro.medium.com/v2/resize:fit:753/1*1sr0IMJEatpy5v5sZtMyXQ.jpeg", width=800)

# Objetivo ejecutivo
st.markdown("## 🎯 Objetivo General")
st.markdown("""
Este dashboard ha sido diseñado para ofrecer a la dirección una **visión clara, rápida y accionable** del comportamiento comercial,
el rendimiento por tienda y las preferencias del cliente, en base a los datos reales de ventas.
""")

# Índice orientador
st.markdown("## 🗂️ ¿Qué encontrará en este Dashboard?")
st.markdown("""
- **📌 Variables Clave:** Revisión inicial y justificación de los datos seleccionados.
- **📊 Gráficos Básicos:** Exploración simple para comprender la distribución y variabilidad.
- **📈 Gráficos Compuestos:** Comparaciones y relaciones entre múltiples dimensiones.
- **🧬 Análisis Multivariado y 3D:** Visualización avanzada y segmentación con técnicas PCA y clustering.
- **📋 Análisis Complementarios:** Insights sobre calificaciones, pagos y rentabilidad cruzada.
- **📋 Resumen Ejecutivo:** Conclusiones, indicadores clave y recomendaciones automatizadas.
""")

# Instrucciones de uso
st.markdown("## 🧭 ¿Cómo utilizar este Dashboard?")
st.markdown("""
Utilice el **menú lateral** para navegar por las diferentes secciones.  
En cada vista encontrará:
- Gráficos interactivos.
- Explicaciones ejecutivas.
- Filtros para ajustar los análisis por fecha, tienda o categoría.

👉 No necesita conocimientos técnicos: cada insight está acompañado de una breve interpretación para facilitar la toma de decisiones.
""")

# Cierre estratégico
st.markdown("## ✅ Toma de Decisiones Basada en Datos")
st.markdown("""
Este dashboard es una herramienta de apoyo a la gestión, diseñada para ayudarle a:
- **Detectar oportunidades**
- **Identificar problemas**
- **Optimizar decisiones comerciales**

Todo esto a partir de información clara, visual y actualizada.
""")
