from django.urls import path 

from task import views 


urlpatterns = [

    path("register/", views.SignUpView.as_view(), name="signup"),

    path("", views.SignInView.as_view(), name="signin"),

    path("task/add", views.TaskcreateView.as_view(), name="task-list"),

    path("task/update/<int:pk>", views.TaskupdateView.as_view(), name="task-update"),

    path("task/delete/<int:pk>", views.TaskdeleteView.as_view(), name="task-delete")
    
]
