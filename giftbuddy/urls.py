"""giftbuddy URL Configuration

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
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from rest_framework import routers
from giftbuddyapi.views import register_user, login_user, RecipientView, InterestView
from giftbuddyapi.views.recipient_interest import RecipientInterestView
from giftbuddyapi.views.search import SearchView
from giftbuddyapi.views.gifter import GifterView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'recipients', RecipientView, 'recipient')
router.register(r'interests', InterestView, 'interest')
router.register(r'recipientinterests', RecipientInterestView, 'recipientinterest')
router.register(r'search', SearchView, 'search')
router.register(r'gifter', GifterView, 'gifter')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)