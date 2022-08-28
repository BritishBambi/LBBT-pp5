from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/rate/', views.review_product,
         name='review_product'),
    path('<int:product_id>/review/<username>/', views.view_review,
         name='view_review'),
    path('<int:product_id>/review/<username>/delete', views.delete_review,
         name='delete_review'),
    path('<int:product_id>/review/<username>/comment', views.review_comment,
         name='review_comment'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
]
