\# 🖥️ Taller – Raspberry Pi 3 con Dash y Grafana



Este proyecto documenta el proceso de instalar, configurar y ejecutar \*\*dashboards en una Raspberry Pi 3\*\*, utilizando \*\*Dash (Python)\*\* y \*\*Grafana\*\* como alternativas a \*\*Streamlit\*\*.  



---



\## 🔹 1. Configuración inicial de la Raspberry Pi

1\. Conectar la Raspberry Pi a:

&nbsp;  - Pantalla, teclado y mouse.

&nbsp;  - Internet (Ethernet recomendado).  

2\. Actualizar sistema:

&nbsp;  ```bash

&nbsp;  sudo apt update \&\& sudo apt upgrade -y

Instalar Python y venv:



sudo apt install python3-venv -y

2\. Creación del entorno virtual



Para mantener las dependencias aisladas se usó venv:



\# Crear entorno virtual

python3 -m venv venv



\# Activar entorno virtual

source venv/bin/activate



\# Actualizar pip

pip install --upgrade pip



🔹 3. Problemas con Streamlit



Se intentó instalar Streamlit dentro del entorno virtual:



pip install streamlit





Pero aparecía el error:



ERROR: Could not find a version that satisfies the requirement streamlit





Esto ocurre porque:



La Raspberry Pi 3 (con sistema operativo de 32-bit) no es compatible con las últimas versiones de Streamlit.



Los binarios precompilados no existen para esa arquitectura.



👉 Solución: se optó por usar Dash (librería de Python para dashboards) y Grafana (plataforma web), que sí son compatibles.

. Dashboard con Dash (Python)

Instalación

pip install dash plotly pandas



Código de ejemplo (app.py)

import dash

from dash import html, dcc

import plotly.express as px

import pandas as pd



app = dash.Dash(\_\_name\_\_)



\# Datos simulados

df = pd.DataFrame({

&nbsp;   "Hora": range(10),

&nbsp;   "Temperatura (°C)": \[22, 23, 24, 23, 25, 26, 27, 26, 24, 23]

})



\# Gráfico

fig = px.line(df, x="Hora", y="Temperatura (°C)", title="Temperatura simulada")



app.layout = html.Div(children=\[

&nbsp;   html.H1("Dashboard con Dash en Raspberry Pi"),

&nbsp;   dcc.Graph(figure=fig)

])



if \_\_name\_\_ == "\_\_main\_\_":

&nbsp;   app.run\_server(debug=True, host="0.0.0.0", port=8050)



Ejecución

python app.py





En la Raspberry:

http://localhost:8050



Desde otra PC en la misma red:

http://<IP\_DE\_TU\_RASPBERRY>:8050



🔹 5. Instalación de Grafana



Grafana fue instalado para probar una alternativa robusta y lista para usar.



Instalación paso a paso

sudo apt-get install -y software-properties-common wget



\# Crear carpeta de llaves

sudo mkdir -p /etc/apt/keyrings/



\# Descargar llave GPG

wget -q -O - https://apt.grafana.com/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/grafana.gpg



\# Agregar repositorio

echo "deb \[signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee /etc/apt/sources.list.d/grafana.list



\# Instalar Grafana

sudo apt-get update

sudo apt-get install grafana -y



Habilitar y arrancar

sudo systemctl enable grafana-server

sudo systemctl start grafana-server

sudo systemctl status grafana-server



🔹 6. Acceso a Grafana



Obtener la IP de la Raspberry:



hostname -I





Ejemplo: 192.168.1.105



Entrar en el navegador:



http://<IP\_DE\_TU\_RASPBERRY>:3000





Credenciales por defecto:



Usuario: admin



Contraseña: admin



Cambiar contraseña al primer inicio.



🔹 7. Dashboard en Grafana



Ir a Connections → Data sources.



Seleccionar TestData DB para generar datos simulados.



Crear un New Dashboard → Add Panel.



Seleccionar tipo de gráfico (línea, barra, gauge).



Guardar y visualizar en la interfaz.



🔹 8. Conclusiones



Streamlit no fue compatible con la Raspberry Pi 3 por limitaciones de arquitectura (32-bit).



Dash es ligero, corre directamente en Python y permite personalización total.



Grafana ofrece un entorno visual robusto, ideal para monitoreo y dashboards listos para producción.



Usar un entorno virtual (venv) mantuvo el sistema ordenado y limpio.



La Raspberry Pi puede funcionar como un servidor de dashboards accesible en red local.

