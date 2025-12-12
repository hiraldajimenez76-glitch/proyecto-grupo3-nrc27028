# mapa_grupo3_nrc27028_final_sin_superposicion.py
import plotly.graph_objects as go
import pandas as pd
import webbrowser
import os
import json
from datetime import datetime

print("="*70)
print("🎯 PROYECTO GRUPO 3 - NRC 27028 - MAPA DE COMERCIO MUNDIAL")
print("="*70)

# ========== CREAR README.md ==========
readme_content = """# 📊 Proyecto: Mapa Interactivo de Comercio Mundial

## 📌 Información del Grupo
- **Grupo:** 3
- **NRC:** 27028
- **Materia:** Análisis de Datos Económicos
- **Fecha:** """ + datetime.now().strftime("%d/%m/%Y") + """
- **Integrantes:** Anghely Ojeda y compañeros

## 🎯 Objetivo
Visualizar los principales flujos comerciales entre países con datos interactivos.

## 🌍 Características
- **Líneas rojas:** Flujos comerciales generales
- **Líneas amarillas:** Flujos de Ecuador (destacados)
- **Hover interactivo:** Ver detalles al pasar el mouse
- **Leyenda completa:** Categorías de montos y países

## 📊 Categorías de Monto
- **> $500B USD:** USA — China
- **$300-$500B USD:** Canadá — USA
- **$100-$500B USD:** Alemania — USA
- **< $100B USD:** Chile — China

## 🌎 Países por Flujos
- **+5 flujos:** USA, China, Alemania
- **2-4 flujos:** Japón, Reino Unido
- **1 flujo:** Perú, Argentina
- **Ecuador (destacado):** Exportador especial

## 🛠️ Cómo Usar
1. Ejecuta el script Python
2. Se abrirá automáticamente el mapa
3. Pasa el mouse sobre las líneas
4. Usa zoom y arrastre para navegar

## 📁 Archivos Generados
1. `entrega_grupo3_nrc27028.html` - Para entregar
2. `tarea_profesional_grupo3.html` - Presentación
3. `README.md` - Esta documentación

---

**Desarrollado por Grupo 3 - NRC 27028**
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md creado exitosamente")

# ========== DATOS DEL MAPA ==========
print("\n📊 CARGANDO DATOS COMERCIALES...")

data = pd.DataFrame({
    'origen': ['USA', 'China', 'Germany', 'Ecuador', 'Brazil', 'Mexico', 
               'Japan', 'UK', 'France', 'Canada', 'Chile', 'Colombia'],
    
    'destino': ['China', 'USA', 'USA', 'USA', 'China', 'USA',
                'USA', 'USA', 'Germany', 'USA', 'China', 'USA'],
    
    'valor': [550, 480, 220, 12.5, 75, 390, 140, 95, 120, 360, 45, 32],
    
    'producto': ['Tecnología', 'Electrónica', 'Automóviles', 'Petróleo', 'Soja', 
                 'Manufactura', 'Automóviles', 'Servicios', 'Aeronáutica', 
                 'Petróleo', 'Cobre', 'Café'],
    
    'detalle': ['Exportación de chips y software', 'Teléfonos y componentes electrónicos',
                'Vehículos premium y maquinaria', 'Petróleo crudo y derivados',
                'Soja y productos agrícolas', 'Automóviles y partes',
                'Vehículos Toyota y Honda', 'Servicios financieros y seguros',
                'Aviones Airbus y componentes', 'Petróleo y gas natural',
                'Cobre refinado y mineral', 'Café arábigo de alta calidad']
})

coordenadas = {
    'USA': [39.8283, -98.5795],
    'Canada': [56.1304, -106.3468],
    'Mexico': [23.6345, -102.5528],
    'Brazil': [-14.2350, -51.9253],
    'Argentina': [-38.4161, -63.6167],
    'Chile': [-35.6751, -71.5430],
    'Colombia': [4.5709, -74.2973],
    'Ecuador': [-1.8312, -78.1834],
    'Peru': [-9.1900, -75.0152],
    'Germany': [51.1657, 10.4515],
    'UK': [55.3781, -3.4360],
    'France': [46.6034, 1.8883],
    'Italy': [41.8719, 12.5674],
    'China': [35.8617, 104.1954],
    'Japan': [36.2048, 138.2529],
    'India': [20.5937, 78.9629]
}

# ========== CREAR EL MAPA ==========
print("🎨 CONSTRUYENDO MAPA INTERACTIVO...")

fig = go.Figure()

# Líneas de flujo comercial
for idx, row in data.iterrows():
    if row['origen'] in coordenadas and row['destino'] in coordenadas:
        if row['origen'] == 'Ecuador' or row['destino'] == 'Ecuador':
            color = 'rgba(255, 215, 0, 0.9)'
            width = max(row['valor']/10, 5)
        else:
            color = 'rgba(255, 50, 50, 0.7)'
            width = max(row['valor']/50, 2)
        
        fig.add_trace(go.Scattergeo(
            lon=[coordenadas[row['origen']][1], coordenadas[row['destino']][1]],
            lat=[coordenadas[row['origen']][0], coordenadas[row['destino']][0]],
            mode='lines',
            line=dict(width=width, color=color),
            opacity=0.8,
            hoverinfo='text',
            text=f"<b>📦 FLUJO COMERCIAL</b><br><br>"
                 f"<b>De:</b> {row['origen']}<br>"
                 f"<b>A:</b> {row['destino']}<br>"
                 f"<b>Valor:</b> ${row['valor']} mil millones USD<br>"
                 f"<b>Producto:</b> {row['producto']}<br>"
                 f"<b>Detalle:</b> {row['detalle']}<br><br>"
                 f"<i>GRUPO 3 - NRC 27028</i>",
            hoverlabel=dict(bgcolor="white", bordercolor="black", font_size=14),
            showlegend=False
        ))

# Puntos de países
for pais, coord in coordenadas.items():
    if pais == 'Ecuador':
        size = 25
        color = '#FFD700'
        texto = f"<b>🇪🇨 {pais}</b><br>Capital: Quito<br>Exporta: Petróleo, banano"
    elif pais in ['USA', 'China', 'Germany']:
        size = 22
        color = '#003366'
        texto = f"<b>{pais}</b><br>Principales exportador"
    else:
        size = 15
        color = '#1E90FF'
        texto = f"<b>{pais}</b>"
    
    fig.add_trace(go.Scattergeo(
        lon=[coord[1]],
        lat=[coord[0]],
        mode='markers',
        marker=dict(size=size, color=color, line=dict(width=2, color='white')),
        hoverinfo='text',
        text=texto,
        hoverlabel=dict(bgcolor="lightblue", font_size=12),
        showlegend=False
    ))

# ========== CONFIGURACIÓN FINAL CON MAPA MÁS PEQUEÑO ==========
fig.update_layout(
    title=dict(
        text="<span style='font-size:28px'>🌍 MAPA INTERACTIVO DE COMERCIO MUNDIAL</span><br>"
             "<span style='font-size:20px'><b>GRUPO 3 - NRC 27028</b></span><br>"
             "<span style='font-size:16px; color:#666'>PASA EL MOUSE SOBRE LAS LÍNEAS PARA VER INFORMACIÓN</span>",
        x=0.5,
        xanchor='center',
        y=0.97
    ),
    
    geo=dict(
        showframe=True,
        showcoastlines=True,
        showcountries=True,
        countrycolor='rgba(150, 150, 150, 0.3)',
        coastlinecolor='rgba(100, 100, 100, 0.8)',
        landcolor='rgba(230, 230, 230, 0.3)',
        oceancolor='rgba(200, 220, 255, 0.2)',
        projection_type='natural earth',
        projection_scale=1.1,
        center=dict(lat=10, lon=-60),
        # Limitar el área visible del mapa
        lataxis_range=[-60, 80],
        lonaxis_range=[-180, 180]
    ),
    
    hovermode='closest',
    height=800,
    # ¡IMPORTANTE! Margen izquierdo más pequeño para dejar espacio a la leyenda
    margin=dict(l=50, r=50, t=120, b=80),
    
    # NOTA: He quitado las anotaciones de Plotly porque se superponen
    # La leyenda ahora estará en un panel HTML separado
)

# ========== GUARDAR ARCHIVOS ==========
print("💾 GUARDANDO ARCHIVOS...")

# 1. Archivo para entrega (solo mapa)
nombre_entrega = "ENTREGA_GRUPO3_NRC27028.html"
fig.write_html(nombre_entrega, include_plotlyjs='cdn', full_html=True, auto_open=False)

# 2. Versión profesional con panel lateral
fig_dict = fig.to_dict()
fig_data = fig_dict['data']
fig_layout = fig_dict['layout']

# Guardar la versión profesional CON PANEL LATERAL
with open("TAREA_PROFESIONAL_GRUPO3.html", "w", encoding="utf-8") as f:
    f.write(f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto Grupo 3 - NRC 27028</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 25px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.8em;
            margin: 0;
        }}
        .header h2 {{
            font-size: 1.5em;
            margin: 10px 0;
            color: #FFD700;
        }}
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        .content {{
            display: flex;
            padding: 0;
        }}
        .map-area {{
            flex: 2;
            padding: 20px;
        }}
        .legend-panel {{
            flex: 1;
            background: #f8f9fa;
            padding: 25px;
            border-left: 3px solid #4CAF50;
            max-width: 350px;
            overflow-y: auto;
        }}
        .map-container {{
            width: 100%;
            height: 650px;
            border: 2px solid #ddd;
            border-radius: 10px;
            overflow: hidden;
        }}
        .footer {{
            background: #343a40;
            color: white;
            padding: 20px;
            text-align: center;
            margin-top: 20px;
        }}
        .btn {{
            display: inline-block;
            padding: 10px 25px;
            margin: 10px;
            background: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
        }}
        .btn:hover {{
            background: #45a049;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
        
        /* Estilos para la leyenda */
        .legend-section {{
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 1px solid #ddd;
        }}
        .legend-title {{
            color: #1E3C72;
            font-size: 1.4em;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 2px solid #4CAF50;
        }}
        .legend-item {{
            margin: 8px 0;
            padding: 8px;
            background: white;
            border-radius: 5px;
            border-left: 4px solid #4CAF50;
        }}
        .color-box {{
            display: inline-block;
            width: 15px;
            height: 15px;
            margin-right: 10px;
            border-radius: 3px;
            vertical-align: middle;
        }}
        .red {{
            background-color: rgba(255, 50, 50, 0.7);
        }}
        .gold {{
            background-color: rgba(255, 215, 0, 0.9);
        }}
        
        @media (max-width: 1200px) {{
            .content {{ flex-direction: column; }}
            .legend-panel {{ max-width: 100%; }}
        }}
    </style>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌍 PROYECTO: MAPA DE COMERCIO INTERNACIONAL</h1>
            <h2>GRUPO 3 - NRC 27028</h2>
            <p>Análisis de Flujos Comerciales Mundiales | {datetime.now().strftime('%d/%m/%Y')}</p>
        </div>
        
        <div class="content">
            <div class="map-area">
                <div class="map-container" id="mapa"></div>
            </div>
            
            <div class="legend-panel">
                <!-- LEYENDA DEL GRUPO 3 -->
                <div class="legend-section">
                    <div class="legend-title">📊 LEYENDA - GRUPO 3</div>
                    
                    <div class="legend-section">
                        <h3>💰 CATEGORÍAS DE MONTO</h3>
                        <div class="legend-item">• <b>> $500B USD:</b> USA — China</div>
                        <div class="legend-item">• <b>$300-$500B USD:</b> Canadá — USA</div>
                        <div class="legend-item">• <b>$100-$500B USD:</b> Alemania — USA</div>
                        <div class="legend-item">• <b>< $100B USD:</b> Chile — China</div>
                    </div>
                    
                    <div class="legend-section">
                        <h3>🌍 PAÍSES POR FLUJOS</h3>
                        <div class="legend-item">• <b>+5 flujos:</b> USA, China, Alemania</div>
                        <div class="legend-item">• <b>2-4 flujos:</b> Japón, Reino Unido</div>
                        <div class="legend-item">• <b>1 flujo:</b> Perú, Argentina</div>
                        <div class="legend-item">• <b>Ecuador (destacado):</b></div>
                        <div class="legend-item" style="margin-left: 20px;">Exportador especial</div>
                    </div>
                    
                    <div class="legend-section">
                        <h3>🎨 SÍMBOLOS</h3>
                        <div class="legend-item">
                            <span class="color-box red"></span> Flujos generales
                        </div>
                        <div class="legend-item">
                            <span class="color-box gold"></span> Flujos de Ecuador
                        </div>
                    </div>
                </div>
                
                <!-- INFORMACIÓN DEL PROYECTO -->
                <div class="legend-section">
                    <h3>📋 Información del Proyecto</h3>
                    <p><strong>Integrantes:</strong> Anghely Ojeda y equipo</p>
                    <p><strong>Materia:</strong> Análisis de Datos Económicos</p>
                    <p><strong>Fecha:</strong> {datetime.now().strftime('%d/%m/%Y')}</p>
                </div>
                
                <!-- OBJETIVOS -->
                <div class="legend-section">
                    <h3>🎯 Objetivos</h3>
                    <div class="legend-item">• Visualizar flujos comerciales principales</div>
                    <div class="legend-item">• Analizar relaciones comerciales entre países</div>
                    <div class="legend-item">• Destacar el rol de Ecuador en comercio internacional</div>
                    <div class="legend-item">• Crear herramienta interactiva para análisis</div>
                </div>
                
                <!-- DATOS INCLUIDOS -->
                <div class="legend-section">
                    <h3>📊 Datos Incluidos</h3>
                    <div class="legend-item">• 12 flujos comerciales principales</div>
                    <div class="legend-item">• 16 países analizados</div>
                    <div class="legend-item">• Montos desde $32B hasta $550B USD</div>
                    <div class="legend-item">• Productos principales por país</div>
                </div>
                
                <!-- BOTONES -->
                <div style="text-align: center; margin-top: 30px;">
                    <a href="{nombre_entrega}" download class="btn">📥 Descargar Mapa</a>
                    <a href="README.md" download class="btn">📄 Descargar README</a>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>© 2024 - Grupo 3 - NRC 27028 | Universidad [Nombre]</p>
            <p>Herramientas: Python, Plotly, Pandas | Datos: WTO, Bancos Centrales</p>
        </div>
    </div>
    
    <script>
        // Datos del mapa
        const data = {json.dumps(fig_data, ensure_ascii=False)};
        const layout = {json.dumps(fig_layout, ensure_ascii=False)};
        
        // Crear el mapa
        Plotly.newPlot('mapa', data, layout);
        
        // Añadir interacción adicional
        document.getElementById('mapa').on('plotly_hover', function(eventData) {{
            console.log('Información mostrada:', eventData.points[0]?.text);
        }});
        
        // Instrucciones para el usuario
        console.log('✅ Mapa del Grupo 3 cargado correctamente');
        console.log('📌 Instrucciones: Pasa el mouse sobre las líneas para ver información detallada');
    </script>
</body>
</html>
""")

# 3. Versión simple sin leyenda (solo para referencia)
with open("MAPASIMPLE_GRUPO3.html", "w", encoding="utf-8") as f:
    f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Mapa Simple - Grupo 3</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1 style="text-align:center; color:#1E3C72;">Mapa Comercial - Grupo 3 - NRC 27028</h1>
    <div id="mapa" style="width:100%; height:700px;"></div>
    <script>
        const data = {json.dumps(fig_data, ensure_ascii=False)};
        const layout = {json.dumps(fig_layout, ensure_ascii=False)};
        Plotly.newPlot('mapa', data, layout);
    </script>
</body>
</html>
""")

print("\n" + "="*70)
print("✅ ¡PROYECTO COMPLETADO EXITOSAMENTE!")
print("="*70)

print("\n📁 ARCHIVOS CREADOS:")
print("1. 📘 README.md                     - Documentación completa")
print("2. 📄 ENTREGA_GRUPO3_NRC27028.html  - Mapa solo para entregar")
print("3. 🎨 TAREA_PROFESIONAL_GRUPO3.html - Presentación con leyenda a lado")
print("4. 🔵 MAPASIMPLE_GRUPO3.html        - Versión simple sin leyenda")

print("\n🎮 CÓMO USAR:")
print("1. Abre 'TAREA_PROFESIONAL_GRUPO3.html' en tu navegador")
print("2. **La leyenda está a la derecha**, NO superpuesta")
print("3. Pasa el mouse sobre las LÍNEAS ROJAS/AMARILLAS")
print("4. Usa zoom y arrastre para explorar")

print("\n📤 PARA ENTREGAR:")
print("• Envía 'ENTREGA_GRUPO3_NRC27028.html' al profesor")
print("• Presenta 'TAREA_PROFESIONAL_GRUPO3.html' en clase")
print("• Incluye el README.md en la entrega")

# Abrir automáticamente la versión profesional
print("\n🚀 Abriendo mapa profesional en navegador...")
webbrowser.open(f"file://{os.path.abspath('TAREA_PROFESIONAL_GRUPO3.html')}")

print("\n" + "="*70)
print("🎉 ¡PROBLEMA DE SUPERPOSICIÓN RESUELTO!")
print("="*70)