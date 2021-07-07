import requests

def Weather(city):

    #city = input("City name:")
    api_address = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=5ca4a78a8c0ae8bf260e79de144b8ba9'.format(city)
    url = api_address
    json_data = requests.get(url).json()
    format_add = json_data['main']
    print("weather is {0}, Temperature is minimum {1} celsius and maximum is {2} celsius".format(json_data['weather'][0]
                                                                                                    ['main'], int(
        format_add['temp_min'] - 273), int(format_add['temp_max'] - 272)))
    return format_add
