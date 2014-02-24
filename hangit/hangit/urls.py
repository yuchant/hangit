from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from outfits import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view()),
    url(r'^outfits/(?P<pk>\d+)/$', views.OutfitView.as_view()),
    url(r'^clothing/$', views.ClothingView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



