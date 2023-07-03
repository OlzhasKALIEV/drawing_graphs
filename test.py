import pandas as pd
import matplotlib.pyplot as plt
import os


class PlotDrawer:
    def __init__(self, data_folder):
        self.data_folder = data_folder

    def draw_plots(self, json_file):
        # Чтение JSON-файла в DataFrame
        df = pd.read_json(json_file)

        # Создание папки для сохранения графиков
        plots_folder = os.path.join(self.data_folder, "графики")
        os.makedirs(plots_folder, exist_ok=True)

        # Рисование графиков
        paths = []
        for column in df.columns:
            plt.figure()
            plt.plot(df[column])
            plt.xlabel('Index')
            plt.ylabel(column)
            plt.title(f"График {column}")
            file_name = f"{column}.png"
            file_path = os.path.join(plots_folder, file_name)
            plt.savefig(file_path)
            paths.append(file_path)

        return paths


# Использование класса PlotDrawer и функции draw_plots
json_file_url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
data_folder = "."
plot_drawer = PlotDrawer(data_folder)
paths = plot_drawer.draw_plots(json_file_url)
# Вывод путей к графикам
print("Пути к графикам:")
for path in paths:
    print(path)
