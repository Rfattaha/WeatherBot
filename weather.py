import requests

def getResp(city):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=%s&appid=TOKEN" % (city))
    getCountry = response.json()["sys"]["country"]
    getCityName = response.json()["name"]
    getWeatherMain = response.json()["weather"][0]["description"]
    getTemp = response.json()["main"]["temp"]

    a = ("Country : {} , \nCity name : {} , \nCity Weather Description : {} , \nCity Calcius : {} °C ".format(getCountry,getCityName,getWeatherMain,getTemp) )
          
    return a
    #print("City name : ",response.json()["name"])
    #print("City Weather Description : ", response.json()["weather"][0]["description"])
    #print("City Calcius is : ",response.json()["main"]["temp"])
    #print("Country : ",response.json()["sys"]["country"] ,"\nCity name : "
    #      ,response.json()["name"],"\nCity Weather Description : "
    #      , response.json()["weather"][0]["description"]
    #      ,"\nCity Calcius is : ",response.json()["main"]["temp"])

resp = getResp("istanbul")

def getTemp():
    return resp.json()["main"]["temp"]

def getWeatherMain():
    return resp.json()["weather"][0]["description"]

def getCountry():
    return resp.json()["sys"]["country"] 

def getCityName():
    return resp.json()["name"]


