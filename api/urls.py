from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')



urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),



    # path('employees/', views.EmployeesView.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetailView.as_view()),

    path('', include(router.urls)),  

    path('blogs/', views.BlogListCreateView.as_view(), name='blog-list-create'),
    path('comments/', views.CommentsView.as_view(), name='comment-list-create'),  


    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),                                                   

]