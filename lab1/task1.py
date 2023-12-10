from typing import Union


class Insect:
    def __init__(self, number_of_legs: int, number_of_eyes: int):
        """
        Объект: насекомое
        param number_of_legs: кол-во ножек
        param number_of_eyes: кол-во глаз
        >>> spider = Insect(8,8)
        """
        if not isinstance(number_of_legs, int):
            raise TypeError("Кол-во ног должно быть целым числом")
        if not isinstance(number_of_eyes, int):
            raise TypeError("Кол-во глаз должно быть целым числом")
        if number_of_legs < 0:
            raise ValueError("Кол-во ног должно быть неотрицательным")
        if number_of_eyes < 0:
            raise ValueError("Кол-во глаз должно быть неотрицательным")
        self.number_of_legs = number_of_legs
        self.number_of_eyes = number_of_eyes

    def is_runner(self) -> bool:
        """
        >>> spider = Insect(8, 8)
        >>> spider.is_runner()
        """
        ...

    def cut_off_legs(self, legs_to_cut: int) -> None:
        """
        >>> spider = Insect(8, 8)
        >>> spider.cut_off_legs(2)
        """
        ...


class DotaHero:
    def __init__(self, strength: int, agility: int, intelligence: int):
        """
        Объект: герой из доты
        param strength: сила
        param agiliry: ловкость
        param intelligence: интеллект
        >>> dark_willow = DotaHero(20, 18, 21)
        """
        if not isinstance(strength, int) or not isinstance(agility, int) or not isinstance(intelligence, int):
            raise TypeError("Атрибуты должны быть целыми числами и никак иначе")
        if strength < 0 or agility < 0 or intelligence < 0:
            raise ValueError("Значения татрибутов должны быть неотрицательными")
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def level_up(self) -> None:
        """
        >>> dark_willow = DotaHero(20, 18, 21)
        >>> dark_willow.level_up()
        """
        ...

    def avg_attribute(self) -> float:
        """
        >>> dark_willow = DotaHero(20, 18, 21)
        >>> dark_willow.avg_attribute()
        """
        ...


class Alcohol:
    def __init__(self, degrees: Union[int, float], taste: str):
        """
        Объект: алкоголь
        param degrees: крепость
        param taste: вкус
        >>> vodka = Alcohol(40, "Греет душу")
        """
        if not isinstance(degrees, Union[int, float]):
            raise TypeError("Крепость должна быть числом")
        if degrees < 0 or degrees > 100:
            raise ValueError("Крепость должна быть в промежутке от нуля до сотни")
        self.degrees = degrees
        self.taste = taste

    def drink(self) -> None:
        """
        >>> vodka = Alcohol(40, "Греет душу")
        >>> vodka.drink()
        """
        ...

    def is_flamable(self) -> bool:
        """
        >>> vodka = Alcohol(40, "Греет душу")
        >>> vodka.is_flamable()
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
