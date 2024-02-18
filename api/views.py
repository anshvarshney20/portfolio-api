from urllib import request
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import project, certificates
from .serializers import ProjectSerializer, CertificateSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from . forms import LoginForm, project_form, CertificateForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class ProjectDetail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id=None, format=None):
        if id is None:
            # Retrieve all projects
            snippets = project.objects.all()
            serializer = ProjectSerializer(snippets, many=True)
        else:
            # Retrieve a specific project by its ID
            snippet = self.get_project_by_id(id)
            serializer = ProjectSerializer(snippet)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_project_by_id(self, id):
        return get_object_or_404(project, id=id)

    def put_object(self, id):
        snippet = self.get_object(id)
        serializer = ProjectSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CertificateDetail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id=None, format=None):
        if id is None:
            # Retrieve all projects
            snippets = certificates.objects.all()
            serializer = CertificateSerializer(snippets, many=True)
        else:
            # Retrieve a specific project by its ID
            snippet = self.get_project_by_id(id)
            serializer = CertificateSerializer(snippet)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_project_by_id(self, id):
        return get_object_or_404(project, id=id)

    def put_object(self, id):
        snippet = self.get_object(id)
        serializer = CertificateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required(login_url='login')
def post(request):
    if request.method == 'POST':
        form = project_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = project_form({})
            # Replace 'success' with the URL name for your success page
            return redirect('/')
    else:
        form = project_form()

    return render(request, 'data.html', {'form': form})


@login_required(login_url='login')
def post_image(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CertificateForm({})
            return redirect('/display-image')
    else:
        form = CertificateForm()

    return render(request, 'data.html', {'form': form})


def update(request, project_id):
    project_instance = project.objects.get(id=project_id)
    form = project_form(instance=project_instance)

    if request.method == 'POST':
        form = project_form(request.POST, request.FILES, instance=project_instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'data.html', context)

@login_required(login_url='login')
def display(request):
    projects = project.objects.all()
    context = {'projects': projects}
    return render(request, 'display.html', context)


@login_required(login_url='login')
def delete(request, project_id):
    try:
        project_instance = project.objects.get(id=project_id)
        project_instance.delete()
        return redirect('display')
    except project.DoesNotExist:
        return redirect('display')

def updateimage(request, certificate_id):
    certificate_instance = certificates.objects.get(id=certificate_id)
    form = CertificateForm(instance=certificate_instance)

    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES, instance=certificate_instance)
        if form.is_valid():
            form.save()
            return redirect('/display-image')

    context = {'form': form}
    return render(request, 'data.html', context)
    
@login_required(login_url='login')
def displayimage(request):
    project_obj = certificates.objects.all()
    context = {'project_obj': project_obj}
    return render(request, 'certificatedisplay.html', context)

@login_required(login_url='login')
def deleteimage(request, project_id):
    try:
        project_instance = certificates.objects.get(id=project_id)
        project_instance.delete()
        return redirect('display-image')
    except certificates.DoesNotExist:
        return redirect('display-image')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('display')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')
