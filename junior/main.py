""" -------`1-----------"""
# def foo():
#     numbers: list[int] = []
#     for i in range(10_000_000):
        # ПЛОХО:
        # 1) Мы создаём огромный список в памяти (10 млн элементов)
        # 2) append выполняется 10 млн раз (лишние операции)
        # 3) Затем sum() делает второй проход по списку
        # => Два действия: заполнение списка + суммирование
        # => Высокое потребление памяти и медленнее на больших данных
        # numbers.append(i**2)

    # Второй проход по уже созданному большому списку
#     return sum(numbers)
# print(foo())

# ЛУЧШЕЕ РЕШЕНИЕ (Generator Expression)
# Здесь НЕ создаётся список в памяти.
# Генератор отдаёт значения по одному (lazy evaluation).
# sum() сразу суммирует без хранения 10 млн элементов.
# => Меньше RAM
# => Быстрее на больших данных
# => Один проход вместо двух
# print(sum(i**2 for i in range(10_000_000)))

"""----------2-----------"""
# def create_racer(name,team,speed,country):
#     return {"name":name,"team":team,"speed":speed,"country":country}
#
# def print_racer_info(racer):
#     print(f"name:{racer['name']}\nteam:{racer['team']}\nspeed:{racer['speed']}\ncountry:{racer['country']}")
#
# def main ():
#     racers = [
#         create_racer("user1","team1","1990","kgz"),
#         create_racer("user2","team2","1990","kgz"),
#         create_racer("user3","team3","1990","kgz"),
#     ]
#     for racer in racers:
#         print_racer_info(racer)
# main()

# def create_racer(name: str, team: str, speed: int, country: str) -> dict:
#     if not isinstance(name, str):
#         raise TypeError("name must be a string")
#     if not isinstance(team, str):
#         raise TypeError("team must be a string")
#     if not isinstance(speed, int):
#         raise TypeError("speed must be an integer")
#     if not isinstance(country, str):
#         raise TypeError("country must be a string")
#
#     return {
#         "name": name,
#         "team": team,
#         "speed": speed,
#         "country": country,
#     }
#
#
# def print_racer_info(racer: dict) -> None:
#     # безопасный доступ через .get()
#     print(
#         f"name: {racer.get('name')}\n"
#         f"team: {racer.get('team')}\n"
#         f"speed: {racer.get('speed')}\n"
#         f"country: {racer.get('country')}"
#     )
#
#
# def main():
#     racers = [
#         create_racer("user1", "team1", 1990, "kgz"),
#         create_racer("user2", "team2", 2100, "kgz"),
#         create_racer("user3", "team3", 1800, "kgz"),
#     ]
#
#     for racer in racers:
#         print_racer_info(racer)
#
#
# if __name__ == "__main__":
#     main()

""" ----------3-------------"""
# def read_line(line):
#     print(line)
#
# def bad_foo():
#     with open("book.txt", "r",encoding="utf-8") as f:
#         data = f.readlines()
#
#     for line in data:
#         print(line)
# bad_foo()
#
#
# def read_line(line: str) -> None:
#     print(line.strip())  # убираем лишний \n
#
#
# def good_foo():
#     with open("book.txt", "r", encoding="utf-8") as f:
#         for line in f:
#             read_line(line)
#
#
# if __name__ == "__main__":
#     good_foo()

