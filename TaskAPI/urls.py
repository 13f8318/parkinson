from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

from TaskApp import views
#router = routers.DefaultRouter()
router = routers.SimpleRouter()

router.register(r'task', views.TaskViewSet)
router.register(r'due_task', views.DueTaskViewSet)
router.register(r'completed_task', views.CompletedTaskViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
