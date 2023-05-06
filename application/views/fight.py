from flask import Blueprint, render_template, redirect, url_for, Response

from application.container import arena, heroes

fight_bp = Blueprint("fight_bp", __name__)


@fight_bp.route("/")
def start_fight() -> str:
    arena.start_game(player=heroes["player"], enemy=heroes["enemy"])  # type: ignore
    return render_template("fight.html", heroes=heroes, result="Бой начался")


@fight_bp.route("/hit/")
def hit() -> str:
    if arena.game_is_running:
        result = arena.player_hit()
    else:
        result = arena.result
    return render_template("fight.html", heroes=heroes, result=result)


@fight_bp.route("/use-skill/")
def use_skill() -> str:
    if arena.game_is_running:
        result = arena.player_use_skill()
    else:
        result = arena.result
    return render_template("fight.html", heroes=heroes, result=result)


@fight_bp.route("/pass-turn/")
def pass_turn() -> str:
    if arena.game_is_running:
        result = arena.next_turn()
    else:
        result = arena.result
    return render_template("fight.html", heroes=heroes, result=result)


@fight_bp.route("/end-fight/")
def end_fight() -> Response:
    return redirect(url_for("main_bp.menu_page"))
