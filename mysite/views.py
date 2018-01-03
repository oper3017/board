from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.http import JsonResponse

class HomeView(TemplateView):
    template_name = 'home.html'

class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserRegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken':User.objects.filter(username__iexact = username).exists()
    }
    if data['is_taken']:
        data['error_message'] = '사용자가 이미 존재합니다. 다른 이름을 입력해 주세요.'

    return JsonResponse(data)
