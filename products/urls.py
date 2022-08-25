from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('<product_id>/rate', views.review_product, name='review_product'),
    path('<product_id>/review/<username>', views.view_review,
         name='view_review'),
]
