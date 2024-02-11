class Human:
    "Базовый класс - Человек"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.age} aged {self.name}"

    def __repr__(self) -> str:
        return f"Human({self.name}, {self.age})"

    "Выход на прогулку"
    def walk(self, hours: float) -> str:
        return f"{self.name} go to a {hours} hour(s) walk"

    "Занятие хобби (предположим, что у все люди любят ситкомы)"
    def do_hobby(self) -> str:
        return f"{self.name} watch a sitcom"


class Gamer(Human):
    "Дочерний класс - геймер"

    def __init__(self, name: str, game: str, experience: int, age: int):
        super().__init__(name, age)
        self.game = game
        self.experience = experience

    def __str__(self) -> str:
        return f"Gamer named {self.name} played {self.game} about {self.experience} years"

    def __repr__(self) -> str:
        return f"Gamer({self.name}, {self.game}, {self.experience}, {self.age})"

    "Хобби геймера - любимая игра, поэтому переопределяем"
    def do_hobby(self) -> str:
        return f"{self.name} plays {self.game}"


if __name__ == "__main__":
    #Создаём объекты классов Human и Gamer
    human = Human("Anton", 25)
    gamer = Gamer("Andrey", "Dota2", 2, 20)

    #Выводим информациб о них
    print(human)
    print(gamer)

    #Вынуждаем их пойти на прогулку
    print(human.walk(1))
    print(gamer.walk(1))

    #Предлагаем им позаниматься их хобби
    print(human.do_hobby())
    print(gamer.do_hobby())
    pass
