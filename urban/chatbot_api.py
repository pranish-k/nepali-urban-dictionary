# chatbot_api.py
import os
from openai import OpenAI
from dotenv import load_dotenv
from django.shortcuts import render
from .models import Word

# Load environment variables from a custom .env file
load_dotenv(dotenv_path='api.env')

# Access the environment variable
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def query_openai_api(input_text):
    """
    Interacts with OpenAI API to generate conversational responses.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a friendly assistant for the Nepali Urban Dictionary. Greet the user warmly and provide conversational responses. Start by saying 'Hello, thank you for using Nepali Urban Dictionary.' Then, mention the word they used and provide its meaning and example if available."
                    ),
                },
                {
                    "role": "user",
                    "content": input_text,
                },
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error querying API: {str(e)}"

# views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        if user_input:
            # Check if the word exists in the database
            word_entry = Word.objects.filter(title__iexact=user_input).first()

            if word_entry:
                response = (
                    f"Hello there! 😊 Thank you for using the Nepali Urban Dictionary.\n"
                    f"The word you asked about is '**{word_entry.title}**'.\n"
                    f"Here's what it means: {word_entry.meaning}."
                )
                if word_entry.sentence:
                    response += f"\nAnd here is how you can use it in a sentence: '{word_entry.sentence}'."
                response += "\nI hope this helps! Feel free to ask about more words."
            else:
                # Query OpenAI API if the word is not found
                response = query_openai_api(user_input)

            return JsonResponse({"response": response})
        else:
            return JsonResponse({"response": "Please enter a word to search."})

    return render(request, "urban/chatbot.html")
