   # chatbot/actions.py
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from urban.models import Word

class ActionLookupWord(Action):
    def name(self) -> str:
        return "action_lookup_word"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        word_title = tracker.get_slot("title")
        try:
            word = Word.objects.get(title__iexact=word_title)
            response = f"The meaning of {word.title} is: {word.meaning}. Here is an example: {word.sentence}"
        except Word.DoesNotExist:
            response = "Sorry, I couldn't find that word in the dictionary."

        dispatcher.utter_message(text=response)
        return []