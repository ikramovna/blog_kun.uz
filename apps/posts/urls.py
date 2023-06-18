from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.posts.views import (CategoryCreateAPIView, StaffModelViewSet, SendMailAPIView, BlogModelViewSet,
                              BlogDetailRetrieveAPIView, RegionModelViewSet, LastBlogListModelViewSet,
                              SearchModelSearchAPIView,
                              )

routers = DefaultRouter()
routers.register('blog', BlogModelViewSet)
routers.register('staff', StaffModelViewSet)
routers.register('region', RegionModelViewSet)
routers.register('last-blog', LastBlogListModelViewSet)
routers.register('category', CategoryCreateAPIView)

urlpatterns = [
    path('', include(routers.urls)),
    path('send_email', SendMailAPIView.as_view()),
    path('blog_detail/<int:pk>', BlogDetailRetrieveAPIView.as_view()),
    path('search', SearchModelSearchAPIView.as_view()),

]
