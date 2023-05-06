from typing import Tuple
from flask import Blueprint, render_template

errors_bp = Blueprint("errors_bp", __name__)


@errors_bp.app_errorhandler(404)
def page_404(e: Exception) -> Tuple[str, int]:
    return render_template("404.html"), 404


@errors_bp.app_errorhandler(ValueError)
def page_value_error(e: Exception) -> Tuple[str, int]:
    return render_template("404.html"), 404


@errors_bp.app_errorhandler(500)
def page_500(e: Exception) -> Tuple[str, int]:
    return render_template("500.html"), 500


@errors_bp.app_errorhandler(405)
def page_405(e: Exception) -> Tuple[str, int]:
    return render_template("500.html"), 405
