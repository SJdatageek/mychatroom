from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
#from chat.views import do_sentiment_analysis
from . import views




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),

    # #url(r'^press_my_buttons/$', press_my_buttons),
    # url(r'^do_sentiment_analysis/$', do_sentiment_analysis),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
