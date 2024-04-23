
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.product_index, name='product_index'),
    path('products/<int:id>/', views.product_show, name='product_show'),
]
