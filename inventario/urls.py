from django.conf.urls import patterns, url

urlpatterns = patterns('inventario.views',
    url(r'^ver/$', 'ver_productos', name='ver_productos'),
)