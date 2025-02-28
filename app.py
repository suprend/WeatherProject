from flask import Flask, render_template_string
import requests

app = Flask(__name__)


@app.route('/')
def weather():
    API_KEY = '11c0d3dc6093f7442898ee49d2430d20'
    city = 'Moscow'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru'

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return f"<h1>Ошибка:</h1><p>{data.get('message', 'Не удалось получить данные')}</p>"

    # Извлекаем необходимые данные
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    html = f"""
    <html>
        <head>
            <meta charset="utf-8">
            <title>Прогноз погоды</title>
        </head>
        <body>
            <h1>Погода в городе {city}</h1>
            <p><strong>Описание:</strong> {description}</p>
            <p><strong>Температура:</strong> {temp}°C</p>
            <p><strong>Влажность:</strong> {humidity}%</p>
            <p><strong>Скорость ветра:</strong> {wind_speed} м/с</p>
        </body>
    </html>
    """
    return render_template_string(html)


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5000)