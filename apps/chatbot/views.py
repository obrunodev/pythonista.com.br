from apps.chatbot.forms import AgentAIForm
from apps.chatbot.models import AgentAI
from apps.chatbot.utils import get_chat_completion_stream
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


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


class AgentAIListView(LoginRequiredMixin, ListView):
    model = AgentAI
    context_object_name = 'agents'

    def get_queryset(self):
        query_set = super().get_queryset()
        query_set = query_set.filter(user=self.request.user)
        return query_set


class AgentAICreateView(LoginRequiredMixin, CreateView):
    model = AgentAI
    form_class = AgentAIForm

    def form_valid(self, form):
        obj_form = form.instance
        obj_form.user = self.request.user
        return super().form_valid(obj_form)

    def get_success_url(self):
        return reverse('chatbot:list')


class AgentAIUpdateView(LoginRequiredMixin, UpdateView):
    ...


class AgentAIDeleteView(LoginRequiredMixin, DeleteView):
    ...
