
# 🧠 Executive Sales Dashboard in Streamlit

Este proyecto consiste en el análisis, visualización y presentación interactiva de datos de ventas mediante Streamlit. Se enfoca en ofrecer un panel gerencial completo, diseñado para facilitar la toma de decisiones a partir de datos reales y filtrados.

---

## 🛠️ Tecnologías Utilizadas

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0076B6?style=for-the-badge&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)

---

## 📦 Requisitos Previos

- **Python 3.9 o superior**
- **pip actualizado**
- **Git** (opcional, si deseas clonar el proyecto)

---

## ⚙️ Configuración del Entorno

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate         # Windows
python -m pip install --upgrade pip
```

---

## 📚 Instalación de Dependencias

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecutar el Servidor Streamlit

```bash
streamlit run app.py
```

---

## 🗂️ Estructura del Proyecto

```
├── app.py                      # Portada ejecutiva del dashboard
├── requirements.txt
├── data/
│   └── data.csv                # Dataset utilizado
├── utils/
│   └── preprocessing.py        # Funciones de carga y transformación
├── pages/
│   ├── 1_Variables_Clave.py
│   ├── 2_Graficos_Basicos.py
│   ├── 3_Graficos_Compuestos.py
│   ├── 4_PCA_y_3D.py
│   └── 5_Resumen_Ejecutivo.py
└── README.md
```

---

## 📊 Páginas del Dashboard

- **📌 Variables Clave:** selección y justificación de las variables más influyentes.
- **📊 Gráficos Básicos:** histogramas, boxplots y dispersión.
- **📈 Gráficos Compuestos:** evolución de ventas por categoría y sucursal.
- **🧬 Análisis Multivariado:** PCA 2D/3D, Scree Plot, matriz de correlación y clustering automático.
- **📋 Resumen Ejecutivo:** KPIs clave y recomendaciones generadas automáticamente desde la data.

---

## 📝 Licencia

Este proyecto fue desarrollado con fines académicos y educativos.
