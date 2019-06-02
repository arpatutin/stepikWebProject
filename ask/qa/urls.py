from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^login/', views.test),
    url(r'^signup/', views.test),
    url(r'^question/(?P<int:id>)', views.test),
    url(r'^ask/', views.test),
    url(r'^popular/', views.test),
    url(r'^new/', views.test)
]