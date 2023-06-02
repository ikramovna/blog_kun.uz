from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.posts.views import (CategoryCreateAPIView, StaffModelViewSet, SendMailAPIView, BlogModelViewSet,
                              BlogDetailRetrieveAPIView, RegionModelViewSet, LastBlogListModelViewSet,
                              SearchModelSearchAPIView,
                              )

routers = DefaultRouter()
routers.register('blog_mixins/', BlogModelViewSet, '')
routers.register('staff_mixins/', StaffModelViewSet, '')
routers.register('region_mixins/', RegionModelViewSet, '')
routers.register('last-blog_mixins/', LastBlogListModelViewSet, '')
routers.register('category_mixins/', CategoryCreateAPIView, '')

urlpatterns = [
    path('', include(routers.urls)),
    path('send_email/', SendMailAPIView.as_view()),
    path('blog_detail/<int:pk>/', BlogDetailRetrieveAPIView.as_view()),
    path('search/', SearchModelSearchAPIView.as_view()),

]
