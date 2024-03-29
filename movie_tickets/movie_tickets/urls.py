"""movie_tickets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from tickets import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name='home'),
    path("signup/",views.signup,name='signup'),
    path("login/",views.loginP,name='login'),
    path("logout/",views.logoutP,name='logout'),
    path("prebooking/<int:id>/",views.booking_page,name='prebooking'),
    path("book/<int:id>/",views.book,name="book"),
    path("book/<pk>",views.book,name="book1"),
    path("ticket/",views.ticket,name="ticket"),
    path("booked/",views.booked,name='booked'),
    path("confirmcancel/<int:id>/",views.cancel,name='cancel'),
    path("cancel/",views.cancel1,name='cancelled'),
    path("theatreedit/",views.theatreedit,name='theatreedit'),
    path("theatre1/",views.theatrelist,name='theatrelist'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)