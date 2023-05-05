from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit


class Skill(ABC):
    """Базовый класс умения"""
    user = None
    target = None

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def stamina(self) -> float:
        pass

    @property
    @abstractmethod
    def damage(self) -> float:
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self) -> bool:
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова skill'а везде используем просто use
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class FuryPunch(Skill):
    _name: str = "FuryPunch"
    _stamina: float = 7
    _damage: float = 10

    @property
    def name(self) -> str:
        return self._name

    @property
    def damage(self) -> float:
        return self._damage

    @property
    def stamina(self) -> float:
        return self._stamina

    def skill_effect(self) -> str:
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage
        return f"{self.user.name} в ярости! {self.target.hp} получил {self.damage} урона!"

    def _is_stamina_enough(self) -> bool:
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        self.user = user
        self.target = target
        if self._is_stamina_enough():
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class HardShot(Skill):
    _name: str = "HardShot"
    _stamina: float = 5
    _damage: float = 12

    @property
    def name(self) -> str:
        return self._name

    @property
    def damage(self) -> float:
        return self._damage

    @property
    def stamina(self) -> float:
        return self._stamina

    def skill_effect(self) -> str:
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage
        return f"{self.user.name} в ярости! {self.target.hp} получил {self.damage} урона!"

    def _is_stamina_enough(self) -> bool:
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        self.user = user
        self.target = target
        if self._is_stamina_enough():
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."
