from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='home'),
    path('', views.about_view, name='about'),
    path('<int:id>/', views.detail_view, name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
