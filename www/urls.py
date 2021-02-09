from django.urls import path, include

urlpatterns = [
    path('', include('www.screens.urls')),
    path('rest/', include('www.rest.urls')),
    path('todo/', include('todo.urls', namespace="todo")),
]
