from django.urls import path
from .views import listfunction,showfunction,likefunction,PostCreate,PostUpdate,PostDelete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', listfunction, name='list'),
    path('show/<int:pk>', showfunction, name='show'),
    path('like/<int:pk>', likefunction, name='like'),
    path('create/', PostCreate.as_view(), name='create'),
    path('update/<int:pk>', PostUpdate.as_view(), name='update'),
    path('delete/<int:pk>', PostDelete.as_view(), name='delete'),
    #imageのURL設定方法 importも忘れずに
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
