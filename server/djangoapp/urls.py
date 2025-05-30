from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path(route='register', view=views.registration, name='register'),
    path(route='login', view=views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path(route='get_cars', view=views.get_cars, name ='getcars'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
