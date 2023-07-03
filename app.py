from flask import Flask, request, make_response
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

from logic import PlotDrawer
from schema.schema import schema_create

app = Flask(__name__)


@app.route("/api/v1/drawing_graphs/", methods=["POST"])
def drawing_graphs():
    graph_json_column = request.get_json()
    try:
        validate(instance=graph_json_column, schema=schema_create)
    except ValidationError as ex:
        return {
            "errors": ex.message
        }, 400

    plot_drawer = PlotDrawer()
    index = plot_drawer.draw_plots(graph_json_column["column_1"], graph_json_column["column_2"])
    return make_response(f"График создан, адрес:{index}")


if __name__ == "__main__":
    app.run(debug=True)
