# from foodcourt.food.views import about
# from foodcourt.food.views import about
from django.contrib import admin
from django.urls import path
from food import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.food),
    path('ordernow', views.order_home),
    path('about',views.about),
    path('receipe',views.receipe),
    path('blog',views.blog),
    path('contact',views.contact),
    path('chatroom',views.chatroom),



    


    path('customersignup', views.customer_signup_view),
    path('customerlogin', LoginView.as_view(template_name='customerlogin.html'), name='customerlogin'),
]
