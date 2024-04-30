from django.urls import path
from wepsite.views import index, potfolio_details, django_filters, RegisterView, resume, search_results, feedback, thanks

urlpatterns = [
    path('', index, name='index_wepsite'),
    path('portfolio-details/', potfolio_details, name='wepsite_potfolio_details'),
    path('filters/', django_filters, name='wepsite_django_filters'),
    path('register/', RegisterView.as_view(), name='register_user'),
    path('resume/', resume, name='wepsit_resume'),
    path('search/', search_results, name='search_results'),
    path('feedback/', feedback, name='feedback'),
    path('thanks/', thanks, name='thanks'),
     
]