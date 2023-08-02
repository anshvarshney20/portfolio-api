from django import forms
from .models import project,certificates

class project_form(forms.ModelForm):
    class Meta:
        model = project
        fields = '__all__'

        clevel_choices = [
            ("Select", "Select"),
            ("Beginner", "Beginner"),
            ("Intermediate", "Intermediate"),
            ("Pro", "Pro"),
        ]
        
        STACK_CHOICES = [
            ('HTML', 'HTML'),
            ('CSS', 'CSS'),
            ('JAVASCRIPT', 'JavaScript'),
            ('REACT JS', 'React JS'),
            ('DJANGO REST API', 'Django REST API'),
            ('DJANGO', 'Django'),
            ('POSTGRESS SQL', 'Postgres SQL'),
            ('WORDPRESS', 'WordPress'),
            ('NEXT JS', 'Next JS'),
            ('TAILWIND CSS', 'Tailwind CSS'),
            ('BOOTSTRAP CSS', 'Bootstrap CSS'),
            ('PYTHON WEB SCRAPPING', 'Python Web Scraping'),
            ('PYTHON DATA SCIENCE', 'Python Data Science'),
            ('NODE JS','Node Js'),
            ('FIREBASE','Firebase'),
            ('EXPRESS JS','Express Js'),
            ('FLUTTER','Flutter'),
            ('GO LANG','Go Lang'),
            ('REACT NATIVE','React Native')
        ]
        
        widgets = {
            'level': forms.Select(choices=clevel_choices),
            'tech_tag': forms.CheckboxSelectMultiple(choices=STACK_CHOICES),
        }

class CertificateForm(forms.ModelForm):
    class Meta:
        model = certificates
        fields = '__all__'
        slevel_choices = [
            ("Select", "Select"),
            ("Beginner", "Beginner"),
            ("Intermediate", "Intermediate"),
            ("Pro", "Pro"),
        ]
        widgets = {
            'level': forms.Select(choices=slevel_choices)
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)