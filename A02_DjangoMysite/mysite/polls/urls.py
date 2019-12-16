from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # name 地址名称
    path('', views.IndexView.as_view(), name='index'),
    # 动态地址(主键)
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # 动态地址(字段名称)
    path('<int:question_id>/vote/', views.vote, name='vote'),
]