def update_hero(*args, hero='Spider-man', power=200, alive=True, speed=100,
                X=1.0, Y=1.0):
    """
    Функция обновления данных, хранящихся в файле "hero.ini".
    :param hero: str
    :param power: int
    :param alive: bool
    :param speed: int
    :param X: float
    :param Y: float
    """
    f_in = open("hero.ini", 'r+', encoding="utf-8")
    # Работает на основе словаря:
    features = {
        'hero': hero,
        'power': power,
        'alive': alive,
        'speed': speed,
        'X': X,
        'Y': Y}
    # запись обновленной информации в файл:
    for k, v in features.items():
        f_in.write(f"{k}={v}\n")
    f_in.close()

if __name__ == "__main__":
    update_hero(hero='Captain America', power=5000, speed=500, alive=False)
