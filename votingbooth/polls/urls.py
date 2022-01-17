from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)