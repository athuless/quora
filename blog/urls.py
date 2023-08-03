from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',home, name='index' ),
    path('create/',create,name='create'),
    path('details/<int:id>/',details,name='details'),
    path('edit/<int:id>/',edit,name='edit'),
    path('delete/<int:id>/',delete,name='delete'),
    path('comment_post/<int:article_id>/',comment_post,name='comment_post'),
    path('comment_delete/<int:id>/',comment_delete,name='comment_delete'),
    path('comment_edit/<int:id>/',comment_edit,name='comment_edit'),
    
]  