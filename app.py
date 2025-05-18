
import streamlit as st

st.set_page_config(page_title="Dashboard Tiendas - Visión Gerencial", layout="wide")

# Encabezado principal
st.title("📊 Dashboard de Ventas - Visión Ejecutiva")
st.markdown("Bienvenido al centro de análisis de ventas para nuestra cadena de tiendas de conveniencia.")

# Imagen ilustrativa
st.image("https://miro.medium.com/v2/resize:fit:753/1*1sr0IMJEatpy5v5sZtMyXQ.jpeg" , width=800)

# Objetivo claro y directo
st.markdown("## 🎯 Objetivo General")
st.markdown("""
Este dashboard ha sido diseñado para ofrecerle a usted, como parte del equipo directivo, una visión clara,
rápida y accionable sobre el comportamiento de las ventas, el rendimiento de las tiendas y las preferencias de los clientes.
""")

# Índice guiado para navegación
st.markdown("## 🗂️ ¿Qué podrá encontrar en este Dashboard?")
st.markdown("""
- **📌 Variables Clave:** Información base del análisis y justificación de los datos considerados críticos.
- **📊 Gráficos Básicos:** Exploración visual inicial para identificar patrones y diferencias clave.
- **📈 Gráficos Compuestos:** Comparaciones entre múltiples variables para detectar relaciones complejas.
- **🧬 Análisis Multivariado y 3D:** Procesamiento avanzado que permite identificar agrupaciones de comportamiento y tendencias ocultas.
- **📋 Resumen Ejecutivo:** Indicadores clave y gráficos estratégicos para tomar decisiones basadas en evidencia.
""")

# Cómo usarlo
st.markdown("## 🧭 ¿Cómo utilizar este Dashboard?")
st.markdown("""
Navegue por las secciones usando el menú a la izquierda. Cada sección contiene visualizaciones interactivas y explicaciones claras.
Además, puede personalizar los análisis usando los **filtros disponibles en la barra lateral** (por fechas, tiendas o categorías).

👉 No se requiere conocimiento técnico para interpretar los resultados. Cada gráfico viene acompañado de un análisis breve que lo orientará en la toma de decisiones.
""")

# Cierre motivador
st.markdown("## ✅ Acción basada en Datos")
st.markdown("""
Este dashboard es una herramienta de apoyo estratégico. Está diseñado para ayudarle a **detectar oportunidades, identificar problemas
y optimizar decisiones comerciales** en base a los datos reales de nuestra operación.
""")
