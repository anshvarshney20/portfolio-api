from django.db import models
import uuid
from multiselectfield import MultiSelectField

class project(models.Model):
    clevel = [
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
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255,null=False)
    image = models.ImageField(upload_to='images/')
    level = models.CharField(max_length=20, choices=clevel)
    link = models.URLField(max_length=255,blank=False)
    tech_tag = MultiSelectField(max_length=255,choices=STACK_CHOICES)
    codelink = models.URLField(max_length=255,blank=False)
    description = models.CharField(max_length=255,blank=False)
    percentage = models.IntegerField(blank=False)
    datetime = models.DateTimeField(auto_now_add=True)

class certificates(models.Model):
    slevel = [
        ("Select", "Select"),
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Pro", "Pro"),
    ]
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255,null=False)
    institute = models.CharField(max_length=255,null=False)
    image = models.ImageField(upload_to='certificates/')
    level = models.CharField(max_length=20, choices=slevel)
    pdf_file = models.FileField(upload_to='pdf_files/')
    datetime = models.DateTimeField(auto_now_add=True)
