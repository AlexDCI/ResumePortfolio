from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import TemplateView

from wepsite.forms import RegisterForm, FeedbackForm, ContactForm
from django.views.generic.edit import FormView
from django.urls import reverse
from wepsite.models import Profile 
import logging

logger = logging.getLogger('my_logger')

def index(request):
    form = ContactForm(request.POST or None)
    logger.info('I am writing this masege after form')
    logger.warning('it is just example')
    if form.is_valid():
        form.save()
        return redirect('thanks')
    context = {'form': form}
    return render(request, 'wepsite/pages/index.html', context=context)



def thanks(request):
    context = {}
    return render(request, 'wepsite/thanks.html', context=context)




def potfolio_details(request):
    context = {}
    return render(request, 'wepsite/pages/portfolio-details.html', context=context)

def django_filters(request):
    context = {'number': 10}
    return render(request, 'filters.html', context=context)

def resume(request):
    context = {}
    return render(request, 'wepsite/resume.html', context=context)

# class RegisterView(TemplateView):
#     template_name = 'wepsite/register.html'
#     def get_context_data(self, *args, **kwargs):
#         my_context = {
#             'register_form': RegisterForm(),
#             'users': ['dave', 'alise']
#         }
#         return my_context

class RegisterView(FormView):
    template_name = 'wepsite/register.html'
    form_class = RegisterForm

    def get_initial(self):
        my_initial: dict = {
            'first_name': 'John',
            'last_name': 'Doe',
        }
        return my_initial
    
    def get_success_url(self):
        return reverse('wepsite_potfolio_details')
    
    def post(self, request):

        form_info = self.form_class(request.POST)
        first_name = form_info.data.get('first_name')
        last_name = form_info.data.get('last_name')
        email = form_info.data.get('email')
        print(request.POST)

        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        print(first_name, last_name, email)
        return super().post(request)
    


def search_results(request):
    query = request.GET.get('skill')
    if query:
        # Используйте метод filter для поиска профилей, содержащих указанный навык
        profiles = Profile.objects.filter(skills__icontains=query)
    else:
        profiles = Profile.objects.all()
    return render(request, 'wepsite/search.html', {'profiles': profiles, 'query': query})



# def feedback(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             return redirect('thanks')
#     else:
#         form = FeedbackForm()
#     return render(request, 'wepsite/feedback.html', {'form': form})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Если форма валидна, можно обработать данные формы
            # В данном случае мы просто выводим сообщение об успешной отправке отзыва
            return render(request, 'wepsite/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'wepsite/feedback.html', {'form': form})