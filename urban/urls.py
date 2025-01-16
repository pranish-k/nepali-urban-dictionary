from django.urls import path
from . import views

urlpatterns = [

    path('', views.search, name='home'),
    path('submit/',views.submit, name='submit'),
    path('allwords/', views.all_words, name='search'),
    path('define/<slug:word_slug>/', views.define, name='define'),
    path('chatbot/', views.chatbot, name='chatbot'),
]