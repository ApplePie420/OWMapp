#imports
import pyowm
import kivy
from kivy.app import App
from kivy.uix.label import Label as CoreLabel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.config import Config
import datetime

#set kivy version and OWM API key
kivy.require("1.10.0")
owm = pyowm.OWM("6f3657da32dda20f2a3d63e6f9aab10f")

#!!!IMPORTANT!!!
#Uncommend following 3 lines to enable 2.8" 320x240 TFT LCD mode
#and comment two lines that are now uncommented (555x350)

#Config.set("graphics", "width", "320")
#Config.set("graphics", "height", "240")
#Config.set("graphics", "fullscreen", "1")
Config.set("graphics", "width", "555")
Config.set("graphics", "height", "350")

#get current time, set location and get weather
now = datetime.datetime.now()
obs = owm.weather_at_place("Prague, CZ")
w = obs.get_weather()

#get weather data
wind = w.get_wind()
hum = w.get_humidity()
temp = w.get_temperature("celsius")
stat = w.get_detailed_status()
l = obs.get_location()
place = l.get_name()
hours = now.hour

#application logic
class AppLogic(GridLayout):
    #set weather values into StringProperty object for Kivy
    placeLbl = StringProperty(place)
    windLbl = StringProperty(str(wind["speed"]))
    humLbl = StringProperty(str(hum))
    tempLbl = StringProperty(str(temp["temp"]))
    statLbl = StringProperty(stat)
    #in case there is a weather state that do not have an image, display error
    sourceImg = "error.png"
    #dont even ask what the actual fuck is this
    if stat == "broken clouds":
        sourceImg = "weather/broken-clouds.png"
    elif stat == "cloudy":
        sourceImg = "weather/overcast clouds.png"
    elif stat == "cold":
        sourceImg = "weather/cold.png"
    elif stat == "light intensity shower rain":
        sourceImg = "weather/drop.png"
    elif stat == "shower rain":
        sourceImg = "weather/drop.png"
    elif stat == "heavy intensity shower rain":
        sourceImg = "weather/drop.png"
    elif stat == "shower rain":
        sourceImg = "weather/drop.png"
    elif stat == "ragged shower rain":
        sourceImg = "weather/drop.png"
    elif stat == "extreme rain":
        sourceImg = "weather/flood.png"
    elif stat == "smoke":
        sourceImg = "weather/fog.png"
    elif stat == "haze":
        sourceImg = "weather/fog.png"
    elif stat == "fog":
        sourceImg = "weather/fog.png"
    elif stat == "sand":
        sourceImg = "weather/fog.png"
    elif stat == "dust":
        sourceImg = "weather/fog.png"
    elif stat == "volcanic ash":
        sourceImg = "weather/fog.png"
    elif stat == "squalls":
        sourceImg = "weather/fog.png"
    elif stat == "mist":
        sourceImg = "weather/foggy.png"
    elif stat == "hot":
        sourceImg = "weather/hot.png"
    elif stat == "light rain":
        sourceImg = "weather/light-rain.png"
    elif stat == "light snow":
        sourceImg = "weather/light-snow.png"
    elif stat == "light wind":
        sourceImg = "weather/light-wind.png"
    elif hours >= "20" and hours <= 7:
        sourceImg = "weather/night.png"
    elif stat == "few clouds":
        sourceImg = "weather/partialy-cloudy.png"
    elif stat == "scattered clouds":
        sourceImg = "weather/partialy-cloudy.png"
    elif stat == "moderate rain":
        sourceImg = "weather/rain.png"
    elif stat == "heavy intensity rain":
        sourceImg = "weather/rain.png"
    elif stat == "very heavy rain":
        sourceImg = "weather/rain.png"
    elif stat == "sleet":
        sourceImg = "weather/sleet.png"
    elif stat == "shower sleet":
        sourceImg = "weather/sleet.png"
    elif stat == "snow":
        sourceImg = "weather/snowing.png"
    elif stat == "heavy snow":
        sourceImg = "weather/snowing.png"
    elif stat == "light rain and snow":
        sourceImg = "weather/snowing.png"
    elif stat == "rain and snow":
        sourceImg = "weather/snowing.png"
    elif stat == "light shower snow":
        sourceImg = "weather/snowing.png"
    elif stat == "shower snow":
        sourceImg = "weather/snowing.png"
    elif stat == "heavy shower snow":
        sourceImg = "weather/snowing.png"
    elif stat == "storm":
        sourceImg = "weather/storm.png"
    elif stat == "violent storm":
        sourceImg = "weather/storm.png"
    elif stat == "thunderstorm with light rain":
        sourceImg = "weather/storm.png"
    elif stat == "thunderstorm with rain":
        sourceImg = "weather/storm.png"
    elif stat == "light thunderstorm":
        sourceImg = "weather/storm.png"
    elif stat == "thunderstorm":
        sourceImg = "weather/storm.png"
    elif stat == "heavy thunderstorm":
        sourceImg = "weather/storm.png"
    elif stat == "ragged thunderstorm":
        sourceImg = "weather/storm.png"
    elif stat == "thunderstorm with light drizzle":
        sourceImg = "weather/storm.png"
    elif stat == "thunderstorm with drizzle":
        sourceImg = "weather/storm.png"
    elif stat == "thunderstorm with heavy drizzle":
        sourceImg = "weather/storm.png"
    elif stat == "clear sky":
        sourceImg = "weather/sunny.png"
    elif stat == "calm":
        sourceImg = "weather/sunny.png"
    elif stat == "high wind, near gale":
        sourceImg = "weather/wind.png"
    elif stat == "gale":
        sourceImg = "weather/wind.png"
    elif stat == "severe gale":
        sourceImg = "weather/wind.png"
    elif stat == "light breeze":
        sourceImg = "weather/wind.png"
    elif stat == "gentle breeze":
        sourceImg = "weather/wind.png"
    elif stat == "moderate breeze":
        sourceImg = "weather/wind.png"
    elif stat == "fresh breeze":
        sourceImg = "weather/wind.png"
    elif stat == "strong breeze":
        sourceImg = "weather/wind.png"

class OpenWeatherApp(App):
    def build(self):
        #on application build, set app name and icon and return application
        self.title = "Minimalistic Weather App"
        self.icon = "icon.png"
        return AppLogic()

#run the actual app
cw = OpenWeatherApp()
cw.run()
