# drawing_graphs


Запуск сервера: python .\app.py 


Данный запросы необходимо выполнять в Постмане (postman)

Для получения всех картинов в папке "charts" необходимо выполнить GET запрос
GET - http://localhost:5000/api/v1/drawing_graphs/all/


(перед тем как выполнять GET запрос необходимо создать график с помощью запроса POST, пример выполнения запроса ниже)

Для создания графика необходимо выполнить POST запрос 
POST - http://localhost:5000/api/v1/drawing_graphs/
далее отправить JSON на url = http://localhost:5000/api/v1/drawing_graphs/

{
    "column_1":"mean",
    "column_2":"max"
}
"column_1" и "column_2" столбцы которые мы сравниваем между собой, создается график который сохроняется в папки "charts"
