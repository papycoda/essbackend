from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ESGProjectViewSet, UserTaskViewSet, create_user, GenerateReportView
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r'projects', ESGProjectViewSet)
router.register(r'tasks', UserTaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  
    path('api/create_user/', create_user,  name='create-user'),
    path('api/generate_report/<str:format>/<int:project_id>/', GenerateReportView.as_view(), name='generate-report'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]

