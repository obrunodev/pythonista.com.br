from apps.chatbot.utils import get_chat_completion
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        messages = [
            {'role': 'system', 'content': 'Você é um assistente virtual que irá responder a perguntas do usuário.'},
            {'role': 'user', 'content': request.POST.get('question')},
        ]
        response = get_chat_completion(messages)
        return HttpResponse(response)
    return render(request, 'chatbot/index.html')