from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('update/<int:id>/', views.update_product, name='update_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('register/',views.register_user,name='register'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('user/',views.user_dashboard,name='user_dashboard'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)