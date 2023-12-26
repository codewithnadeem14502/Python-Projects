import requests
import pyttsx3
import json

if __name__ == "__main__":
    city = input("Enter the city please: ")
    engine = pyttsx3.init()
    url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

    r = requests.get(url)
    w_dic = json.loads(r.text)

    # Check if the response contains an error message
    if "error" in w_dic:
        engine.say(f"Invalid City Name: {w_dic['error']['message']}")
        engine.runAndWait()
    else:
        value = w_dic["current"]["temp_c"]
        print(f"Today's {city} weather is about {value} Celsius")
        engine.say(f"Today's {city} weather is about {value} Celsius")
        engine.runAndWait()
