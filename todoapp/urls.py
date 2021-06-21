

from django.urls import path
from todoapp.views import create_todo,list_all_todos,update_todo,delete_todo,index,registration,login_view,signout

urlpatterns = [
    path('create', create_todo, name="create"),
    path('list',list_all_todos,name="listalltodos"),
    path('update/<int:id>',update_todo,name="update"),
    path('delete/<int:id>',delete_todo,name="delete"),
    path('home',index,name="home"),
    path('account',registration,name="registration"),
    path('signin',login_view,name='login'),
    path('signout',signout,name='logout')

]


