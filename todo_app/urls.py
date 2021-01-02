from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.tododata,name='views'),
    path('upload',views.model_form_upload,name='upload'),
    path('pending_task/<task_id>',views.pending_task,name='pending_task'),
    path('complate_task/<task_id>', views.complate_task, name='complate_task'),
    path('delete_task/<task_id>', views.delete_task, name='delete_task'),
    path('edit_task/<task_id>',views.edit_task,name='edit_task'),

    path('register/',views.regPage,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutuser,name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

