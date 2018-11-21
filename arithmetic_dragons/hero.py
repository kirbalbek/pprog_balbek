# coding: utf-8
# license: GPLv3
from gameunit import *

class Hero(Attacker):
    def __init__(self, name):
        self._health = 100
        self._attack = 50
        self._name = name
        self._experience = 0

    def attack(self, target):
        target._health -= self._attack


#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получает атрибут target и уменьшать его здоровье на величину атаки.
Выходят два одинаковых по цвету дракона, каждого из которых необходимо победить.
После игры experience увеличивается.
"""
