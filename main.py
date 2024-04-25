import random
import requests

#    ПРИВЕТСТВИЕ
GREETINGS = ("> Привет!", "> Здравствуй!", "> Рада тебя видеть!", "> Добро пожаловать!")

#        ПОМОЩЬ / СПРАВКА
HELP_MESSAGES = (
    "> Я могу рассказать вам погоду, новости, поставить будильник или найти информацию в интернете.",
    "> Спросите меня о погоде, новостях или попросите найти что-нибудь в интернете.",
    "> Я эксперт во многих областях, так что не стесняйтесь спрашивать."
)

#          ПОГОДНЫЙ КЛЮЧ
WEATHER_API_KEY = "6d8e495ca73d5bbc1d6bf8ebd52c4"
WEATHER_LOCATIONS = {
    "Москва": "Moscow",
    "Санкт-Петербург": "Saint Petersburg",
    "Новосибирск": "Novosibirsk",
    "Екатеринбург": "Yekaterinburg",
    "Казань": "Kazan"
}

#            КЛЮЧ НОВОСТЕЙ
NEWS_API_KEY = "dbb3c25c61cd447fa02390f363a55979"

#          СЮДА ПОПАДАЕТ ВРЕМЯ БУДИЛЬНИКА
ALARMS = {}

#              АНЕКДОТЫ И ШУТКИ
JOKES = (
    "> Почему курица перешла дорогу? Чтобы попасть на другую сторону!",
    "> Что говорит ремень штанов пуговице? Обхвати меня!",
    "> Почему рыбак носит шляпу? Чтобы держать голову от шеи!",
    "> Плохие лимоны после смерти попадают в лимонад.",
    "> Дважды наступил на одни грабли? Выкинь их. Похоже, они тебя невзлюбили.",
    "> Весна — самое красивое время года, если не видеть места для выгула собак…",
    "> Чтоб ваши размышления о высоких материях не были прерваны никаким образом — не забывайте закрывать дверь туалета"
    "> Опаздывать надо не спеша. Зачем торопиться опаздывать?",
    "> Скачал книгу из интернета — спас дерево.",
    "> Мудрость приходит с годами. А потом уходит…"
)

#          ВИКТОРИНЫ
TRIVIA_QUESTIONS = (
    {"question": "> Кто написал Гарри Поттера?", "answer": "Джоан Роулинг"},
    {"question": "> Какая самая высокая гора в мире?", "answer": "Эверест"},
    {"question": "> Кто был первым человеком на Луне?", "answer": "Нил Армстронг"},
    {"question": "> Очень ценный металл рыжего цвета?", "answer": "Золото"},
    {"question": "> Как называют дневной приём пищи?", "answer": "Обед"},
    {"question": "> Птица с очень ярким и красивым хвостом?", "answer": "Павлин"},
    {"question": "> Как называют детёныша лошади?", "answer": "Жеребёнок"},
    {"question": "> Очень кислый фрукт, но полезный при простуде?", "answer": "Лимон"},
    {"question": "> Овощ, в котором «сто одёжек»?", "answer": "Капуста"}
)

#          ИГРЫ
GAMES = {
    "камень-ножницы-бумага": {
        "moves": ["камень", "ножницы", "бумага"],
        "rules": {
            "камень": {"ножницы": "выигрыш", "бумага": "проигрыш"},
            "ножницы": {"бумага": "выигрыш", "камень": "проигрыш"},
            "бумага": {"камень": "выигрыш", "ножницы": "проигрыш"}
        }
    },
    "виселица": {
        "words": ["яблоко", "банан", "груша", "арбуз", "виноград"],
        "guesses": 10
    }
}


#           ОСНОВНОЙ ТЕКСТ И ФУНКЦИОНАЛ
def main():
    print("")
    print("Привет! Я Алиса, твой персональный помощник.")
    print("    Я умею много чего, например:")
    print("> Играть в игры по команде 'игра виселица' и 'игра камень-ножницы-бумага'")
    print("> Заводить будильник по команде 'будильник'")
    print("> Оповещать о погодных условиях по команде 'погода'")
    print("> Рассказывать о последних новостях по команде 'новости'")
    print("> Поднимать настроение шутками по команде 'шутка' или 'расскажи шутку'")
    print("> Проводить интересные викторины по команде 'викторина'")
    print("   ...и еще много чего будет улучшено в ближайшее время :3 ")
    print("")

    while True:
        user_input = input("Вы: ").lower()
        if user_input in ("выход", "до свидания"):
            print("> До свидания!")
            break
        elif user_input in ("привет", "здравствуй"):
            print(random.choice(GREETINGS))
        elif user_input in ("помощь", "справка"):
            print(random.choice(HELP_MESSAGES))
        elif user_input.startswith("погода"):
            if len(user_input.split()) > 1:
                location = user_input.split()[1]
                get_weather(location)
        elif user_input.startswith("новости"):
            get_news()
        elif user_input.startswith("будильник"):
            set_alarm(user_input)
        elif user_input in ("шутка", "расскажи шутку"):
            print(random.choice(JOKES))
        elif user_input.startswith("викторина"):
            play_trivia()
        elif user_input.startswith("игра"):
            game_name = user_input.split()[1]
            if game_name in GAMES:
                play_game(GAMES[game_name])
            else:
                print("> Извините, я не знаю эту игру.")
        else:
            print("> Извините, я не понимаю.")


#         ПОГОДА
def get_weather(location):
    if location in WEATHER_LOCATIONS:
        location = WEATHER_LOCATIONS[location]
    response = requests.get(
        'https://api.openweathermap.org/data/2.5/find?q=Petersburg&type=like&APPID=6d8e495ca73d5bbc1d6bf8ebd52c4')
    data = response.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    print(f"Погода в {location}: {description}, Температура: {temp} градусов, Влажность: {humidity}%")


#         НОВОСТИ
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=ru&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if 'articles' in data:
        articles = data["articles"]
        for article in articles:
            print(f"{article['title']}: {article['description']}")
    else:
        print("> Не удалось получить новости.Я уже разбираюсь в этой проблеме, попробуйте пока другую команду.")


#             БУДИЛЬНИК
def set_alarm(user_input):
    if len(user_input.split(" ")) > 1:
        time = user_input.split()[1]
        ALARMS[time] = True
        print(f"Будильник установлен на {time}.")


#               РАБОТА ВИКТОРИНЫ
def play_trivia():
    question = random.choice(TRIVIA_QUESTIONS)
    print(question["question"])
    answer = input("Вы: ")
    if answer.lower() == question["answer"].lower():
        print("Правильно!")
    else:
        print("Неправильно. Правильный ответ: {}".format(question["answer"]))


#           РАБОТА ИГР
def play_game(game):
    if game == GAMES["камень-ножницы-бумага"]:
        print("Правила игры:")
        for move, rules in game["rules"].items():
            print(f"{move}: {rules}")
        while True:
            user_move = input("Выберите 1 из 3: ")
            if user_move not in game["moves"]:
                print("Неверный ход. Попробуйте еще раз.")
            else:
                computer_move = random.choice(game["moves"])
                print(f"Я выбрал {computer_move}.")
                result = game["rules"][user_move][computer_move]
                if result == "выигрыш":
                    print("Вы выиграли!")
                elif result == "проигрыш":
                    print("Вы проиграли.")
                elif result == "ничья":
                    print("Ничья.")
                break
    elif game == GAMES["виселица"]:
        word = random.choice(game["words"])
        guesses = game["guesses"]
        guessed_letters = []
        while guesses > 0:
            print(f"Слово: {''.join(guessed_letters)}")
            print(f"У вас осталось {guesses} попыток.")
            guess = input("> ")
            if guess in word:
                guessed_letters.append(guess)
                if all(letter in guessed_letters for letter in word):
                    print("Вы выиграли!")
                    break
            else:
                guesses -= 1
        if guesses == 0:
            print("Вы проиграли. Слово было:", word)


if __name__ == "__main__":
    main()
