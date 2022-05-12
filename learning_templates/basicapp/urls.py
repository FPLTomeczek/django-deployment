from . import views
from django.urls import path

# TEMPLATE TAGGING
app_name = 'basicapp'

urlpatterns = [
    path('relative', views.relative, name='relative'),
    path('other', views.other, name='other')
]
