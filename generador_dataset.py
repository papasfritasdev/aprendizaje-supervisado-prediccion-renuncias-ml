"""
Generador de datos sintéticos de Recursos Humanos.
Crea un dataset de 350 empleados simulando perfiles laborales reales y calcula 
la variable objetivo 'renuncia' aplicando lógica condicional vectorizada basada 
en el riesgo (insatisfacción, horas extra, salario y ascensos). Exporta a CSV.
"""

import pandas as pd
import numpy as np

# Configurar semilla para reproducibilidad (asegura que siempre genere los mismos datos)
np.random.seed(42)
n = 350 # Mínimo de 300 registros exigido

# ==========================================
# 1. GENERACIÓN DE VARIABLES BASE
# ==========================================
edad = np.random.randint(22, 61, n)

# Años en la empresa: Vectorización pura a prueba de fallos
max_anios = np.minimum(edad - 18, 20)
anios_en_empresa = (np.random.random(n) * (max_anios + 1)).astype(int)

# Salario mensual con límite inferior (piso realista del SBU ecuatoriano aprox.)
salario_base = np.random.normal(800, 200, n)
salario_mensual = np.round(salario_base + (anios_en_empresa * 50) + (edad * 10), 2)
salario_mensual = np.clip(salario_mensual, 460, None) 

# Variables operativas e historial del empleado
horas_extra_semana = np.random.randint(0, 21, n)
satisfaccion_laboral = np.random.randint(1, 6, n)
num_proyectos_anio = np.random.randint(1, 11, n)
distancia_casa_trabajo_km = np.random.randint(1, 81, n)
ultima_evaluacion_desempeno = np.round(np.random.uniform(0.0, 1.0, n), 2)
capacitaciones_recibidas = np.random.randint(0, 6, n)

# Probabilidad de ascenso basada en el desempeño
prob_ascenso = np.where(ultima_evaluacion_desempeno > 0.7, 0.4, 0.05)
tiene_ascenso_ultimos_2_anios = np.random.binomial(1, prob_ascenso)


# ==========================================
# 2. VARIABLE OBJETIVO (LÓGICA CONDICIONAL)
# ==========================================
prob_renuncia = np.full(n, 0.1) # Probabilidad base del 10%

# Máscaras booleanas para evaluar las condiciones de riesgo
condicion_critica = (satisfaccion_laboral <= 2) & (horas_extra_semana > 10)
condicion_insatisfecho = (satisfaccion_laboral <= 2) & ~condicion_critica

# Aplicar reglas de negocio vectorizadas (Suman o restan riesgo)
prob_renuncia = np.where(condicion_critica, prob_renuncia + 0.50, prob_renuncia)
prob_renuncia = np.where(condicion_insatisfecho, prob_renuncia + 0.25, prob_renuncia)
prob_renuncia = np.where(tiene_ascenso_ultimos_2_anios == 1, prob_renuncia - 0.15, prob_renuncia)
prob_renuncia = np.where(distancia_casa_trabajo_km > 40, prob_renuncia + 0.10, prob_renuncia)

# Asegurar que las probabilidades se mantengan en un rango lógico (5% a 95%)
prob_renuncia = np.clip(prob_renuncia, 0.05, 0.95)

# Generar la variable objetivo final 'renuncia' (0 = No, 1 = Sí)
renuncia = np.random.binomial(1, prob_renuncia)


# ==========================================
# 3. ENSAMBLAJE Y EXPORTACIÓN DEL DATASET
# ==========================================
df = pd.DataFrame({
    'edad': edad,
    'anios_en_empresa': anios_en_empresa,
    'salario_mensual': salario_mensual,
    'horas_extra_semana': horas_extra_semana,
    'satisfaccion_laboral': satisfaccion_laboral,
    'num_proyectos_anio': num_proyectos_anio,
    'distancia_casa_trabajo_km': distancia_casa_trabajo_km,
    'ultima_evaluacion_desempeno': ultima_evaluacion_desempeno,
    'capacitaciones_recibidas': capacitaciones_recibidas,
    'tiene_ascenso_ultimos_2_anios': tiene_ascenso_ultimos_2_anios,
    'renuncia': renuncia
})

# Guardar en CSV
df.to_csv('dataset_empleados.csv', index=False)
print(f"¡Éxito! Archivo 'dataset_empleados.csv' generado con {len(df)} registros perfectos y optimizados.")