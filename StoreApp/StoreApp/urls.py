
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.product_index),
    path('products/', views.product_index, name='product_index'),
    path('products/<int:id>/', views.product_show, name= 'product_show')
]
