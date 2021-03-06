from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from portfolio_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
