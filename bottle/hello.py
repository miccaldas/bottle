import snoop
from bottle import Bottle, request, response, static_file, template

app = Bottle()


@app.route("test/about/static/<filepath:path>")
def server_static(filepath):
    """"""


@app.route("/test/about")
def about():
    """"""
    tpl = "Hello {{ name }}!"
    template(tpl, name="World")


if __name__ == "__main__":
    app.run(debug=True)
