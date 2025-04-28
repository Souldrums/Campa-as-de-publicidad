
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Cargar los datos limpios
df_clean = pd.read_csv('ad_campaign_data_clean.csv')

# Seleccionar características y variable objetivo
# Supongamos que queremos predecir los ingresos basados en impresiones y clics
X = df_clean[['impressions', 'clicks']]  # Características
y = df_clean['revenue']  # Variable objetivo (ingresos)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)  # Error cuadrático medio
r2 = r2_score(y_test, y_pred)  # R2 (coeficiente de determinación)

print(f"Error cuadrático medio (MSE): {mse}")
print(f"Coeficiente de determinación (R2): {r2}")

# Mostrar los coeficientes del modelo
print("Coeficientes del modelo de regresión:")
print(f"Intercepto: {model.intercept_}")
print(f"Coeficientes: {model.coef_}")

# Guardar las predicciones en un archivo CSV para su análisis posterior
predictions = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
predictions.to_csv('campaign_predictions.csv', index=False)
