"""mysport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static
from django.urls import path
from polls.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register,name='register'),
    url(r'product$',products,name='products'),

    url(r'products-detail/(?P<pid>\d+)/$',products_detail,name='products_detail'),
    url(r'contact$',contact_us,name='contact_us'),
    url(r'^$',home,name='home'),
    url(r'shop_cart$',cart,name='cart'),
    #path('forget/',forget,name='forget'),
    path('profile/',profile,name='profile'),
    #path('admin_index/',admin_index,name='admin_index'),
    path('login/',signin,name='signin'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


