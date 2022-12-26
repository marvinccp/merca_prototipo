from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product_create/', views.product_create, name='product_create'),
    path('category_create/', views.category_create, name='category_create'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='product_delete'),
    path('update/<int:id>', views.update, name='product_update'),
    path('category_detail/<category>', views.category_detail, name='category_detail'),
    path('categories/', views.categories, name='categories'),
]

