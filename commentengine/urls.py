from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from commentengine import views

router = DefaultRouter()
router.register(r'comment', views.ChildDetailViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'comments/$', views.MasterCommentList.as_view()),
                       url(r'^comments/(?P<pk>[0-9]+)/$', views.MasterCommentDetail.as_view()),
                       )
