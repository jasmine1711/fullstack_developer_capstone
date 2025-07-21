from django.urls import path, re_path

from django.contrib import admin      

from . import views  # .views gives access to login_view and logout_view

app_name = 'djangoapp'

urlpatterns = [
    # Auth routes
    path("login/", views.login_user, name="login"),

    path('logout/', views.logout_view, name='logout'),
    
    path('register/', views.register_user, name='register'),
    # Add other views here (e.g., registration, review)
    re_path(r'^.*$', views.FrontendAppView.as_view(), name='frontend'),
    
    path('admin/', admin.site.urls)
]
    # path('register', views.register_view, name='register'),
    # path('add_review', views.add_review_view, name='add_review'),
    

