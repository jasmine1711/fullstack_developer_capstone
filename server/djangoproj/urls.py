"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from djangoproj.settings import BASE_DIR

urlpatterns = [
    # Serve React frontend
    path('', TemplateView.as_view(template_name='index.html')),
    path('login/', TemplateView.as_view(template_name='index.html')),
    path('register/', TemplateView.as_view(template_name='index.html')),  # if using React route for register
    # Admin
    path('admin/', admin.site.urls),
    # Backend API endpoints
    path('djangoapp/', include('djangoapp.urls')),
]

# Static files from React build
urlpatterns += [
    re_path(r'^(?P<path>manifest\.json|favicon\.ico|robots\.txt|logo192\.png|logo512\.png)$',
        serve,
        {'document_root': os.path.join(BASE_DIR, 'frontend', 'build')}),
]

# Media files (if any)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
