import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
data = pd.read_csv("C:\\Salary_dataset.csv")

# Extraer las columnas
years_of_experience = data['YearsExperience']
salary = data['Salary']

# Calcular la pendiente (m) y la intersección (b)
mean_x = years_of_experience.mean()
mean_y = salary.mean()
diff_x = years_of_experience - mean_x
diff_y = salary - mean_y
m = (diff_x * diff_y).sum() / (diff_x**2).sum()
b = mean_y - m * mean_x

# Crea la línea de regresión
regression_line = m * years_of_experience + b

print(f"Pendiente (m): {m}")
print(f"Intersección (b): {b}")

# Grafica los datos y la línea de regresión
plt.scatter(years_of_experience, salary, label='Datos de salario')
plt.plot(years_of_experience, regression_line, color='red', label='Línea de regresión')
plt.xlabel('Años de experiencia')
plt.ylabel('Salario')
plt.legend()
plt.title('Regresión Lineal de Salario vs Años de Experiencia')
plt.grid(True)
plt.show()

