"""fbPay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

import pay.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', pay.views.index, name='index'),
    url(r'^createBooking$', 'pay.views.createBooking', name='createBooking'),
    url(r'^fbcallback', pay.views.fbcallback, name='fbcallback'),
    url(r'^messengerhook',pay.views.messengerhook,name='messengerhook'),
    url(r'^fb_pay$',pay.views.fb_pay,name='fb_pay'),
    url(r'^fb_pay_2$',pay.views.fb_pay_2,name='fb_pay_2'),
    url(r'^fb_pay_3$',pay.views.fb_pay_3,name='fb_pay_3')
]
