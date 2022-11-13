from django.urls import path,include,re_path
from django.conf.urls.static import static 
from django.conf import settings


from EmployeeApp import views

urlpatterns = [
    re_path(r'^department/$',views.DepartmentApi),
    re_path(r'^department/([0-9]+)$',views.DepartmentApi),
    
    re_path(r'^employee/$',views.EmployeeApi),
    re_path(r'^employee/([0-9]+)$',views.EmployeeApi),
    
     re_path(r'^SaveFile$',views.SaveFile),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
