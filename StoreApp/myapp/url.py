from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="products/", permanent=True)),
    path('products/', views.index, name='index'),
    path('products/<int:pk>/', views.show, name='show'),
    path('products/', views.product_index, name='product_index'),
    path('products/<int:id>/', views.product_show, name='product_show'),
]