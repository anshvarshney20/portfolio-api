# Generated by Django 4.2.3 on 2023-08-02 04:30

from django.db import migrations, models
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='certificates',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('institute', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='certificates/')),
                ('level', models.CharField(choices=[('Select', 'Select'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Pro', 'Pro')], max_length=20)),
                ('pdf_file', models.FileField(upload_to='pdf_files/')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('level', models.CharField(choices=[('Select', 'Select'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Pro', 'Pro')], max_length=20)),
                ('link', models.URLField(max_length=255)),
                ('tech_tag', multiselectfield.db.fields.MultiSelectField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JAVASCRIPT', 'JavaScript'), ('REACT JS', 'React JS'), ('DJANGO REST API', 'Django REST API'), ('DJANGO', 'Django'), ('POSTGRESS SQL', 'Postgres SQL'), ('WORDPRESS', 'WordPress'), ('NEXT JS', 'Next JS'), ('TAILWIND CSS', 'Tailwind CSS'), ('BOOTSTRAP CSS', 'Bootstrap CSS'), ('PYTHON WEB SCRAPPING', 'Python Web Scraping'), ('PYTHON DATA SCIENCE', 'Python Data Science'), ('NODE JS', 'Node Js'), ('FIREBASE', 'Firebase'), ('EXPRESS JS', 'Express Js'), ('FLUTTER', 'Flutter'), ('GO LANG', 'Go Lang'), ('REACT NATIVE', 'React Native')], max_length=255)),
                ('codelink', models.URLField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('percentage', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]