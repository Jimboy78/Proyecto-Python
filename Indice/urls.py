from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', include("Posts.urls")),
    path('', include("Cuentas.urls")),
    path('', views.Inicio, name="index"),
    path('about_us/', views.AboutUs.as_view(), name="about_us"),
    path('blog/',views.Blog.as_view(), name="blog"),
    path('logout/', LogoutView.as_view(template_name="index.html"), name='logout'),
]
 