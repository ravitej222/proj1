from django.urls import path
from app1 import views
#create app1 requests

app_name = 'app1'

urlpatterns = [
    path('courses',views.courses,name='courses'),
    path('newcourse',views.newcourse,name='newcourse'),
    path('newcourse2 ',views.newcourse2,name='newcourse2'),
    path('newcourse3 ',views.newcourse3,name='newcourse3'),
    path('updatecourse/<int:id>',views.updatecourse,name='updatecourse'),
    path('deletecourse/<int:id>',views.deletecourse,name='deletecourse'),

]