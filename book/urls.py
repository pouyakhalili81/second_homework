from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.show_time),
    path('pen/',views.pen),
    path('book/book1',views.book1),
    path('book/list',views.show_objects),
    path('book/list/myway',views.show_object_myway),
    path('book/list/way1',views.show_objects_1)
]