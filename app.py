import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Inicializar la aplicación
app = dash.Dash(__name__)

# Datos simulados
df = pd.DataFrame({
    "Hora": range(10),
    "Temperatura (°C)": [22, 23, 24, 23, 25, 26, 27, 26, 24, 23]
})

# Crear un gráfico de líneas
fig = px.line(df, x="Hora", y="Temperatura (°C)", title="Temperatura simulada")

# Layout de la app
app.layout = html.Div(children=[
    html.H1("Dashboard con Dash en Raspbe
