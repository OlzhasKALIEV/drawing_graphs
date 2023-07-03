# drawing_graphs

Необходимо выполнить пост запрос 
POST - localhost:5000/api/v1/drawing_graphs/
далее отправить JSON по адресу localhost:5000/api/v1/drawing_graphs/

{
    "column_1":"mean",
    "column_2":"max"
}
"column_1" и "column_2" столбцы которые мы сравниваем между собой, создается график который сохроняется в папки "графики"
