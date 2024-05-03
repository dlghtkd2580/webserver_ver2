from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'web'

urlpatterns = [
        path('', views.main, name='main'),
        path('new_form', views.new_form, name='new_form'),
        path('login', views.login, name='login'),
        path('logout', views.logout, name='logout'),
        path('admin/<int:form_pk>', views.form_view, name='form_view'),
        path('admin', views.list, name='list'),
        path('admin/<int:form_pk>/delete', views.form_delete, name='form_delete'),
        path('admin/form_delete_all', views.form_delete_all, name='form_delete_all'),
        path('admin/file_delete',views.file_delete, name='file_delete'),
        path('admin/file_delete_all',views.file_delete_all, name='file_delete_all'),
        path('admin/file_view',views.file_view, name='file_view'),
        path('admin/edit',views.file_edit, name='file_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
