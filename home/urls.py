from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('diarys/', views.DiaryListView.as_view(), name='diarys'),
    path('diary/<int:pk>', views.DiaryDetailView.as_view(), name='diary-detail'),
    
    #path('add_diary/', views.add_diary, name='add_diary'),
    path('post/add/',views.model_form_add,name='add_post'),
]

