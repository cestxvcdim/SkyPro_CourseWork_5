from flask import render_template, Blueprint

main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def menu_page() -> str:
    return render_template("index.html")
