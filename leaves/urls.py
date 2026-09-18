from django.urls import path
from leaves import views

urlpatterns = [
    path('apply/',views.apply_leave,name='apply_leave'),
    path('my_leaves/',views.my_leaves,name='my_leaves'),
    path('view_leaves/',views.view_leaves,name='view_leaves'),
    path('approve/<int:id>/',views.approve_leave,name='approve_leave'),
    path('reject/<int:id>/',views.reject_leave,name='reject_leave'),
]