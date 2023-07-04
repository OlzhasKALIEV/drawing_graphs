import pandas as pd
import matplotlib.pyplot as plt
import os


class PlotDrawer:
    def __init__(self):
        self.json_file = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
        self.fig = None

    def draw_plots(self, column_1: str, column_2: str):
        # Чтение JSON-файла в DataFrame
        df = pd.read_json(self.json_file)

        # Очистка предыдущего графика
        if self.fig is not None:
            plt.close(self.fig)

        # Создание нового графика
        self.fig = plt.figure()
        ax = self.fig.add_subplot(111)

        # Рисование графика
        ax.plot(df[column_1], label=column_1)
        ax.plot(df[column_2], label=column_2)
        ax.set_xlabel('Index')
        ax.set_ylabel('Meaning')
        ax.set_title(f"Comparison Graph {column_1} and {column_2}")
        ax.legend()

        # Создание папки для сохранения графиков
        plots_folder = os.path.join(".", "charts")
        os.makedirs(plots_folder, exist_ok=True)

        file_name = f"Column Comparison column {column_1} and column {column_2}.png"
        file_path = os.path.join(plots_folder, file_name)
        self.fig.savefig(file_path)

        return file_path