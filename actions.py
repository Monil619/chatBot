# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return 'action_chitchat'

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        intent = tracker.latest_message['intent'].get('name')

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in ['ask_builder', 'ask_howdoing',
                      'ask_howold', 'ask_languagesbot', 'ask_restaurant',
                      'ask_time', 'ask_wherefrom', 'ask_whoami',
                      'handleinsult', 'telljoke', 'ask_whatismyname']:
            dispatcher.utter_template('utter_' + intent, tracker)

        return []

class ActionWeatherAPI(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def weather(self, city):
        # city = input("City name:")
        api_address = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=5ca4a78a8c0ae8bf260e79de144b8ba9'.format(
            city)
        url = api_address
        json_data = requests.get(url).json()
        format_add = json_data['main']
        print("weather is {0}, Temperature is minimum {1} celsius and maximum is {2} celsius".format(
            json_data['weather'][0]
            ['main'], int(
                format_add['temp_min'] - 273), int(format_add['temp_max'] - 272)))
        return format_add

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.latest_message['text']
        temp1 = self.weather(city)
        temp = int(temp1['temp'] - 273)
        print(temp)
        dispatcher.utter_template("utter_temp", tracker, temp=temp)
        return []

class ActionOMNWebsite(Action):
    def name(self) -> Text:
        return "action_about_omn_website"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link = "https://openmynetwork.com/WebSite/about_us.php"
        # dispatcher.utter_message(text="Hello World!")
        dispatcher.utter_template("utter_about_omn_website", tracker, link=Link)
        return []

