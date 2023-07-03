import pandas as pd

url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
df = pd.read_json(url)
mean_deviation = df['mean'].mean()
max_deviation = df['mean'].max()
min_deviation = df['mean'].min()
std_deviation = df['mean'].std()
print(f"Среднее отклонение:, {mean_deviation}")
print(f"Максимальное отклонение:, {max_deviation}")
print(f"Минимальное отклонение:, {min_deviation}")
print(f"Стандартное отклонение:, {std_deviation}")
