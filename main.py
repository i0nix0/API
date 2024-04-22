import random
import requests
import schedule
from datetime import datetime

# Greetings
GREETINGS = ("Привет!", "Здравствуй!", "Рада тебя видеть!", "Добро пожаловать!")

# Help
HELP_MESSAGES = (
    "Я могу рассказать вам погоду, новости, поставить будильник или найти информацию в интернете.",
    "Спросите меня о погоде, новостях или попросите найти что-нибудь в интернете.",
    "Я эксперт во многих областях, так что не стесняйтесь спрашивать."
)

# Weather
WEATHER_API_KEY = "YOUR_API_KEY"
WEATHER_LOCATIONS = {
    "Москва": "Moscow",
    "Санкт-Петербург": "Saint Petersburg",
    "Новосибирск": "Novosibirsk",
    "Екатеринбург": "Yekaterinburg",
    "Казань": "Kazan"
}

# News
NEWS_API_KEY = "YOUR_API_KEY"

# Alarms
ALARMS = {}

# Jokes
JOKES = (
    "Почему курица перешла дорогу? Чтобы попасть на другую сторону!",
    "Что говорит ремень штанов пуговице? Обхвати меня!",
    "Почему рыбак носит шляпу? Чтобы держать голову от шеи!"
)

# Trivia
TRIVIA_QUESTIONS = (
    {"question": "Кто написал Гарри Поттера?", "answer": "Джоан Роулинг"},
    {"question": "Какая самая высокая гора в мире?", "answer": "Эверест"},
    {"question": "Кто был первым человеком на Луне?", "answer": "Нил Армстронг"}
)

# Games
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


# Custom Functions
def get_weather(location):
    if location in WEATHER_LOCATIONS:
        location = WEATHER_LOCATIONS[location]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}"
    response = requests.get(url)
    data = response.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    print(f"Погода в {location}: {description}, Температура: {temp} градусов, Влажность: {humidity}%")


def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=ru&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    for article in articles:
        print(f"{article['title']}: {article['description']}")


def set_alarm(user_input):
    time = user_input.split(" ")[1]
    ALARMS[time] = True
    print(f"Будильник установлен на {time}.")


def play_trivia():
    question = random.choice(TRIVIA_QUESTIONS)
    print(question["question"])
    answer = input("> ")
    if answer.lower() == question["answer"].lower():
        print("Правильно!")
    else:
        print("Неправильно. Правильный ответ:", question["answer"])


def play_game(game):
    if game["name"] == "камень-ножницы-бумага":
        print("Правила игры:")
        for move, rules in game["rules"].items():
            print(f"{move}: {rules}")
        while True:
            user_move = input("> ")
            if user_move not in game["moves"]:
                print("Неверный ход.")
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
    elif game["name"] == "виселица":
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
            print("Вы проиграли. Слово:", word)


def print_ku(message, start_time, end_time):
    now = datetime.now()
    hour = now.hour
    if now.strftime("%H:%M") >= start_time and now.strftime("%H:%M") <= end_time:
        return
    print(message * hour)


def main():
    print("Привет! Я Алиса, твой персональный помощник.")
    while True:
        user_input = input("> ").lower()
        if user_input in ("выход", "до свидания"):
            print("До свидания!")
            break
        elif user_input in ("привет", "здравствуй"):
            print(random.choice(GREETINGS))
        elif user_input in ("помощь", "справка"):
            print(random.choice(HELP_MESSAGES))
        elif user_input.startswith("погода"):
            location = user_input.split(" ")[1]
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
            game_name = user_input.split(" ")[1]
            if game_name in GAMES:
                play_game(GAMES[game_name])
            else:
                print("Извините, я не знаю эту игру.")
        elif user_input.startswith("кукушка"):
            message = user_input.split(" ")[1]
            start_time = user_input.split(" ")[2]
            end_time = user_input.split(" ")[3]
            schedule.every().hour.at(":00").do(print_ku, message, start_time, end_time)
        else:
            print("Извините, я не понимаю.")


if __name__ == "__main__":
    main()