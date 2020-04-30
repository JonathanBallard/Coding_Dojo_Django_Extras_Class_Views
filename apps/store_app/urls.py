


''' 
================================================================================ 
================================================================================ 
                            APP-LEVEL URLS.PY: store_app 
================================================================================ 
================================================================================ 
''' 



from django.urls import path 
from django.conf.urls import url 
from . import views 
from .views import Products, ThisProduct

urlpatterns = [ 
    path('', views.index), 
    path('products/', views.Products.as_view()), 
    path('products/<int:id>/', views.ThisProduct.as_view()), 
    path('products/<int:id>/delete/', views.delete), 

] 
