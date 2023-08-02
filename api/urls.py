from . import views 
from django.urls import path
from .views import *

urlpatterns = [
    path('',views.display,name='display'),
    path('create/', views.post, name='data'),
    path('imagecreate/', views.post_image, name='dataimage'),
    path('login/', views.user_login, name='login'), 
    path('logout/', views.logout_user, name='logout'), 
    path('delete/<uuid:project_id>/',views.delete,name='delete'),
    path('update/<uuid:project_id>/',views.update,name='update'),
    path('project-fetch/', ProjectDetail.as_view(), name='project-detail'),
    path('project/<uuid:id>/', ProjectDetail.as_view(), name='project-detail'),
    path('project-update/<uuid:id>/', ProjectDetail.as_view(), name='project-detail'),
    path('image-fetch/', CertificateDetail.as_view(), name='project-detail'),
    path('certificate-all/<uuid:id>/', CertificateDetail.as_view(), name='project-detail'),
    path('certificate-update/<uuid:id>/', CertificateDetail.as_view(), name='project-detail'),
    path('display-image/',views.displayimage,name='display-image'),
    path('delete-image/<uuid:project_id>/',views.deleteimage,name='deleteimage'),
    path('update-image/<uuid:certificate_id>/',views.updateimage,name='updateimage'),
]
