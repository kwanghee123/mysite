from django.urls import path
from . import views

urlpatterns = [
    path('result/<int:id>', views.result),
    path('add_question', views.add_question),
    path('input', views.input),
    path('data', views.data),
    path('', views.index, name='index'),
    path('<int:number>/data/<str:email>', views.data),
    path('<int:id>', views.detail, name='detail55'),     # poll/2 로 주소가 바뀌면서 detail로 위치이동
    path('vote/', views.vote, name='vote'),              # vote/ 면 detail form action에 / 해줘야 함
]
