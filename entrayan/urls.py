from django.conf.urls import include, url
from django.contrib import admin


from course_notification_app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'entrayan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^v1/admin/', include(admin.site.urls)),
    url(r'^v1/subscribe_courses', views.subscribe_courses),
    #url(r'^v1/subscribe_course', views.subscribe_course), 
    url(r'^v1/create_course', views.create_course),
    #url(r'^v1/submit_course', views.submit_course)
]
