from selenium import webdriver
from playsound import playsound
chromedriver="chromedriver.exe"
driver=webdriver.Chrome(chromedriver)
driver.get("https://www.theweathernetwork.com/in/36-hour-weather-forecast/uttar-pradesh/sitapur-2")
weather=driver.find_element_by_xpath('//*[@id="thirty-six-hours-periods"]/div[2]/div[4]/div[2]/span')
temp=driver.find_element_by_xpath('//*[@id="thirty-six-hours-periods"]/div[2]/div[4]/div[4]/span[1]')
Humidity=driver.find_element_by_xpath('//*[@id="thirty-six-hours-periods"]/div[2]/div[4]/div[9]/span[1]')
wind=driver.find_element_by_xpath('//*[@id="thirty-six-hours-periods"]/div[2]/div[4]/div[7]/span[1]')
weather_input=weather.text
temperature=temp.text
humid=Humidity.text
wind_speed=wind.text
driver.get("file:///C:/Users/lenovo/Desktop/onspot/index.html")
driver.find_element_by_class_name("weather").send_keys(weather_input)
driver.find_element_by_class_name("temp").send_keys(temperature)
driver.find_element_by_class_name("wind").send_keys(wind_speed)
driver.find_element_by_class_name("humidity").send_keys(humid)
if weather_input=="Clear":
    playsound('alarm.mp3')
    

