from django import forms
from wepsite.models import Article, Contact


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label = 'Your First Name',
        help_text = 'thi is requaers you first name',
       # intial = 'Bob'
        )
    last_name = forms.CharField()
    # intial = 'Doe'
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    choise = (
        ('mail', 'Male'),
        ('fimail', 'Female'),
    )
    choise_field = forms.ChoiceField(choices=choise, label='You gender')
    
    boolian_field = forms.BooleanField()
    integer_field = forms.IntegerField()
    text = forms.CharField(widget=forms.Textarea({'cols': 100, 'rows': 25}))
    
   
class ArticleFormHardWay(forms.Form):
    title = forms.CharField(max_length=250)
    owner = forms.CharField(max_length=100)
    rating = forms.FloatField(initial=5.0)
    validated = forms.BooleanField(initial=False)
    short_description = forms.CharField(widget=forms.Textarea())
    published_date = forms.DateField()


class ArticleFormEasyWay(forms.ModelForm):
    class Meta:
        model = Article
        #fields = ['title', 'rating', 'short_description']
        fields = "__all__"
        #exclude = ['owner', 'validated', 'published_date']




class FeedbackForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea({'cols': 100, 'rows': 25}))
    email = forms.EmailField(label='Email')
    date = forms.DateField(label='Date')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'