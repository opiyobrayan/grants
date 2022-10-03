
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('grants', views.grant,name='grant'),
    path('add-grants', views.register_project,name='add-grant'),
    path('update-grants/<grant_id>', views.update_grants,name='update-grant'),
    path('submitted', views.submisionform,name='submitted'),
   
]