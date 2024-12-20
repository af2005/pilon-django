from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"user", views.UserViewSet)
router.register(r"group", views.GroupViewSet)
router.register(r"label", views.LabelViewSet)
router.register(r"entity", views.EntityViewSet)
router.register(r"project", views.ProjectViewSet)
router.register(r"markdown-entity", views.MarkdownEntityViewSet)
router.register(r"wiki-page", views.WikiPageViewSet)
router.register(r"journal-page", views.JournalPageViewSet)
router.register(r"task", views.TaskViewSet)
router.register(r"comment", views.CommentViewSet)
router.register(r"attachment", views.AttachmentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
