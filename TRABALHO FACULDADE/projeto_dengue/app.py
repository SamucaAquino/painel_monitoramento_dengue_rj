from flask import Flask, jsonify, render_template
from flask_cors import CORS
import json
import os


app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(BASE_DIR, 'bases')


@app.route('/')
def index():
    return render_template('index.html')

with open('C:/Users/ree11390/OneDrive - M DIAS BRANCO S.A. INDUSTRIA E COMERCIO DE ALIMENTOS/Área de Trabalho/TRABALHO FACULDADE/bases/kpis_atemporais.json', encoding='utf-8') as f:
    dados_atemporais = json.load(f)

with open('C:/Users/ree11390/OneDrive - M DIAS BRANCO S.A. INDUSTRIA E COMERCIO DE ALIMENTOS/Área de Trabalho/TRABALHO FACULDADE/bases/kpis_temporais.json', encoding='utf-8') as f:
    dados_temporais = json.load(f)

with open('C:/Users/ree11390/OneDrive - M DIAS BRANCO S.A. INDUSTRIA E COMERCIO DE ALIMENTOS/Área de Trabalho/TRABALHO FACULDADE/bases/kpi_classificacao_risco_municipio.json', encoding='utf-8') as f:
    dados_classificacao_risco_municipio = json.load(f)

with open('C:/Users/ree11390/OneDrive - M DIAS BRANCO S.A. INDUSTRIA E COMERCIO DE ALIMENTOS/Área de Trabalho/TRABALHO FACULDADE/bases/kpi_variacao_percent_semana_semana.json', encoding='utf-8') as f:
    dados_variacao_percent_semana_semana = json.load(f)

with open('C:/Users/ree11390/OneDrive - M DIAS BRANCO S.A. INDUSTRIA E COMERCIO DE ALIMENTOS/Área de Trabalho/TRABALHO FACULDADE/projeto_dengue/static/geo/municipios_rj.geojson', encoding='utf-8') as f:
    geojson_municipios = json.load(f)

@app.route('/kpis/atemporais')
def get_kpis_atemporais():
    return jsonify(dados_atemporais)
    
@app.route('/kpis/temporais')
def get_kpis_temporais():
    return jsonify(dados_temporais)

@app.route('/kpi/classificacao-risco')
def get_kpis_classificacao_risco_municipio():
    return jsonify(dados_classificacao_risco_municipio)
    
@app.route('/kpi/variacao-semana')
def get_kpis_variacao_percent_semana_semana():
    return jsonify(dados_variacao_percent_semana_semana)

@app.route('/geojson/municipios-rj')
def get_geojson_municipios():
    return jsonify(geojson_municipios)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)