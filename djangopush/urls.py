"""djangopush URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from push.views import home, send_push_form, subscribe, send_push

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('send_push_form', send_push_form),
    path('send_push', send_push),
    path('subscribe', subscribe),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
