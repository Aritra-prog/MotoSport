from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.register_user,name="register"),
    path('login',views.loginuser,name="login"),
    path('dashboard',views.dashboard,name="dashboard"),
    # path('add_company/', add_company, name='add_company'),
    path('add_company/', views.add_company, name='add_company'),
    path('delete_company/<int:id>/', views.delete_company, name='delete_company'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('apply/<int:company_id>/', views.apply_company, name='apply_company'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    