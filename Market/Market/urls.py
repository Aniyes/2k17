"""Market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from product import views
from product.views import collection_view
from accounts.views import login, create_person, logout_view, home
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from product.views import ProductViewSet, CollectionViewSet, create_product, detail_view, list_view, retrieve_product


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'collections', CollectionViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^detail/(?P<object_id>\d+)/$', detail_view, name='detail_view'),
    url(r'^list/$', list_view, name='list_view'),
    url(r'^login/$', login, name='user_login'),
    url(r'^register/$', create_person, name='register'),
    url(r'^logout/$', logout_view, name='logout_view'),
    url(r'^collection_view/$', collection_view, name='collection_view'),
    url(r'^create/$', create_product, name='create_product'),
    url(r'^retrieve/(?P<title>[\w.@+-]+)/$', retrieve_product, name='retrieve_product'),
    url(r'^home/$', home, name='home'),
    #url(r'^retrieve/(?P<slug>[\w-]+)/$', retrieve_product, name='Retrieve_Product'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/', include(routers.url)),
    #url(r'^register/$ views.register/', name='register'),
    #url(r'^blog/', Blog, name='Blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
