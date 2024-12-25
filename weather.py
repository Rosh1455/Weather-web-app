from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = 'your_api_key'

@app.route('/')
def home():
    return render_template('w.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if city:
        
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
            return render_template('w.html', weather=weather_data)
        else:
            error_message = "City not found. Please try again."
            return render_template('w.html', error=error_message)
    return render_template('w.html')

if __name__ == '_main_':
    app.run(debug=True)