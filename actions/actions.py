# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAdmissionDecision(Action):
     def name(self) -> Text:
         return "action_admission_decisions"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="The admission decisions for winter semester will release on 27th August and for summer semester will be released on 17th January.")

         return []


class ActionEventDates(Action):
     def name(self) -> Text:
         return "action_event_dates"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Halloween: 29th October,New Year Party: 31st December,Valentines Day: 14th February,Jesus Birthday: 31st February,World AIDS day: 1st December,Diwali Festival: 21st October,Campus Party: 3rd October,Christmas Party: 25th December")

         return []


class ActionUniWebsite(Action):
    def name(self) -> Text:
        return "action_uni_website"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Our university website link: https://www.th-deg.de")
        return []


class ActionLanguageCourses(Action):
    def name(self) -> Text:
        return "action_language_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="You can find all the information about the language courses here: https://www.th-deg.de/language-and-electives-centre")

        return []


class ActionAvailableCourses(Action):
    def name(self) -> Text:
        return "action_available_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="To find more about the courses we offer, please follow the link: https://www.th-deg.de/study-programmes")

        return []

class ActionCareerService(Action):
    def name(self) -> Text:
        return "action_career_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Please use this email to contact the career service: stefanie.moeginger@th-deg.de")

        return []

class ActionSummerSchool(Action):
    def name(self) -> Text:
        return "action_summer_school"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="We offer summer schools for various topics here at the Deggendorf Institute of Technology.")

        return []

class ActionBachelorStudy(Action):
    def name(self) -> Text:
        return "action_bachelor_study"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Bachelor courses are in areas of Technology and Engineering, Healthcare, Business and Economics and Computer Science."
    "If you are not sure which bachelor's degree is right for you, if you are a German or other EU citizen you could take the opportunity "
                 "to use 1 - 2 semesters completing Orientation Studies to find out which degree programme would be your final selection."
    "The 1st semester of studies for the following courses can only be started in October, the winter semester.")

class ActionMasterStudy(Action):
    def name(self) -> Text:
        return "action_master_study"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Bachelor courses are in areas of Technology and Engineering, Health, Business and Economics and Computer Science."
        "If you are not sure which master's degree is right for you, if you are a German or other EU citizen you could take the "
                 "opportunity to use 1 - 2 semesters completing Orientation Studies to find out which degree programme would be your final selection."
                 "The 1st semester of studies for the following courses can only be started in March, the summer semester.")

        return []

class ActionAskingEverythingOk(Action):
    def name(self) -> Text:
        return "action_asking_everything_ok"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Is there anything else, which I can help you?"
              " If yes, keep asking, if no, then bye and see you again next time!")
        return []

class ActionHolidaySchedule(Action):
    def name(self) -> Text:
        return "action_holiday_schedules"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="The holidays are from 21st January to 27th February")

        return []