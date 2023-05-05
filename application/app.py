from flask import Flask, render_template, request, redirect, url_for, Response
from unit import BaseUnit, PlayerUnit, EnemyUnit
from base import Arena
from classes import unit_classes
from equipment import Equipment

app = Flask(__name__)

heroes = {
    "player": BaseUnit,
    "enemy": BaseUnit
}

arena = Arena()


def chose_entity(entity_type: str, url: str) -> Response | str:
    if request.method == "GET":
        header = entity_type
        equipment = Equipment()
        weapons = equipment.get_weapons_names()
        armors = equipment.get_armors_names()
        classes = unit_classes
        return render_template(
            "hero_choosing.html",
            result={
                "header": header,
                "classes": classes,
                "weapons": weapons,
                "armors": armors
            }
        )
    if request.method == "POST":
        name = request.form["name"]
        armor_name = request.form["armor"]
        weapon_name = request.form["weapon"]
        unit_class = request.form["unit_class"]
        if entity_type == "Выберите героя":
            player = PlayerUnit(name=name, unit_class=unit_classes.get(unit_class))
            player.equip_weapon(Equipment().get_weapon(weapon_name))
            player.equip_armor(Equipment().get_armor(armor_name))
            heroes["player"] = player
        else:
            enemy = EnemyUnit(name=name, unit_class=unit_classes.get(unit_class))
            enemy.equip_weapon(Equipment().get_weapon(weapon_name))
            enemy.equip_armor(Equipment().get_armor(armor_name))
            heroes["enemy"] = enemy
        return redirect(url_for(url))


@app.route("/")
def menu_page() -> str:
    return render_template("index.html")


@app.route("/fight/")
def start_fight() -> str:
    arena.start_game(player=heroes["player"], enemy=heroes["enemy"])
    return render_template("fight.html", heroes=heroes, result="Бой начался!")


@app.route("/fight/hit")
def hit() -> str:
    if arena.game_is_running:
        result = arena.player_hit()
        return render_template("fight.html", heroes=heroes, result=result)
    return render_template("fight.html", heroes=heroes, result=arena.battle_result)


@app.route("/fight/use-skill")
def use_skill() -> str:
    if arena.game_is_running:
        result = arena.player_use_skill()
        return render_template("fight.html", heroes=heroes, result=result)
    else:
        return render_template("fight.html", heroes=heroes, result=arena.battle_result)


@app.route("/fight/pass-turn")
def pass_turn() -> str:
    if arena.game_is_running:
        result = arena.next_turn()
        return render_template("fight.html", heroes=heroes, result=result)
    else:
        return render_template("fight.html", heroes=heroes, result=arena.battle_result)


@app.route("/fight/end-fight")
def end_fight() -> str:
    return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['POST', 'GET'])
def choose_hero() -> Response | str:
    return chose_entity("Выберите героя", "choose_enemy")


@app.route("/choose-enemy/", methods=['POST', 'GET'])
def choose_enemy() -> Response | str:
    return chose_entity("Выберите врага", "start_fight")
