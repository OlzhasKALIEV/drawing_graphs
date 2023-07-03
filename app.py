from flask import Flask, request, make_response, jsonify

from logic import PlotDrawer

app = Flask(__name__)


@app.route("/api/v1/drawing_graphs/", methods=["POST"])
def drawing_graphs():
    graph_json_column_1 = request.get_json()
    plot_drawer = PlotDrawer()
    index = plot_drawer.draw_plots(graph_json_column_1["column_1"], graph_json_column_1["column_2"])
    return make_response(f"График создан, адрес:{index}")


if __name__ == "__main__":
    app.run(debug=True)
