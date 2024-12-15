from apps.chatbot.utils import get_chat_completion_stream
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.method == 'POST':
        messages = [
            {'role': 'system', 'content': 'Você é um assistente virtual que irá responder a perguntas do usuário.'},
            {'role': 'user', 'content': request.POST.get('question')},
        ]
        response = StreamingHttpResponse(get_chat_completion_stream(messages), content_type='text/event-stream')
        response['X-Accel-Buffering'] = 'no'
        response['Cache-Control'] = 'no-cache'
        return response
    
    return render(request, 'chatbot/index.html')
