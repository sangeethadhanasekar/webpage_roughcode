
from flask import Flask, render_template,request
import  requests
api_key="1c926433ffd0ade5b6aa50fdb540f803"


app=Flask(
    __name__,
    template_folder="client/templates",
    static_folder="client/static",

)
def get_weather(city):
    url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"
    #url="http://api.openweathermap.org/data/2.5/weather?q="+city+api_key+"&units=metric"
    weather_details=requests.get(url).json()
    return {'description': weather_details['weather'][0]['description'],
            'temperature': weather_details['main']['temp']}


@app.route('/' , methods=['GET','POST'])
def weather():
    if request.method =='GET':
        return render_template('index.html')

    else:
        location=request.form['cities']
        weather_data=get_weather(location)
        return render_template('index.html',city = location,
                               description=weather_data['description'],
                               temperature=weather_data['temp'])



if __name__ == "__main__":
    app.run(debug=True)
