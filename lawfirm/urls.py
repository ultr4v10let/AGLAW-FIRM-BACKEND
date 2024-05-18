"""
URL configuration for lawfirm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from teammembers.views import TeamMembersList
from legalservices.views import LegalServicesList
from news.views import NewsList
from clients.views import ClinetsList
from gallery.views import GalleryList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('team-members/', TeamMembersList.as_view()),
    path('legal-services/', LegalServicesList.as_view()),
    path('news/', NewsList.as_view()),
    path('clients/', ClinetsList.as_view()),
    path('gallery/', GalleryList.as_view())

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
