from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
import random
import requests



def all_words(request):
    words = Word.objects.all()
    context = {'words': words}
    return render(request, 'urban/all_words.html', context)


def submit(request):
    form = WordForm()
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'urban/submit.html', context)


def search(request):
    form = SearchForm()
    context = {'form': form}  # Initialize context with form

    if request.method == 'POST':
        form = SearchForm(request.POST)
        print("Form is submitted")
        if form.is_valid():
            print("Form is valid")
            query = form.cleaned_data['query']
            words = Word.objects.filter(title__icontains=query)
            context.update({'words': words, 'query': query})  # Update context with search results
        else:
            print("Form is not valid")
    else:
        # Get a random word from the database
        random_word = random.choice(Word.objects.all())
        context.update({'random_word': random_word})  # Update context with random word

    return render(request, 'urban/search.html', context)


def define(request, word_slug):
    word_title = word_slug.replace('-', ' ')
    word = get_object_or_404(Word, title__iexact=word_title)
    context = {'word': word}
    return render(request, 'urban/define.html', context)

def chatbot(request):
    return render(request, 'urban/chatbot.html')
