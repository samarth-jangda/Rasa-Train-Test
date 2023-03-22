# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ValidateMoneyTranserForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_money_transfer_form"
    @staticmethod
    def state_db() -> List[Text]:
        """Defining the list of states to match the slot value"""
        return ["haryana","hyderabad","rajasthan","uttar pradesh","up",
                "mp","hp","himachal"]
    
    def validate_state(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """To validate the state slot filled by user"""
        
        if slot_value.lower() in self.state_db():
            return {"transfer_state": slot_value}
        else:
            return {"transfer_state": None}

    def validate_amount(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """To validate the amount if amount not more than 10 lakh"""
        
        if slot_value.lower() < "10lakh":
            return {"transfer_amount": slot_value}
        else:
            return {"transfer_amount": None}     
        