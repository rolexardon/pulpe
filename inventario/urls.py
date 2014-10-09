<<<<<<< HEAD
from django.conf.urls import patterns, url

urlpatterns = patterns('inventario.views',
    url(r'^ver/$', 'ver_productos', name='ver_productos'),
	url(r'^ejecutar/compra$', 'post_compra', name='post_compra'),
	
=======
from django.conf.urls import patterns, url

urlpatterns = patterns('inventario.views',
    url(r'^ver/$', 'ver_productos', name='ver_productos'),
	url(r'^ejecutar/compra$', 'post_compra', name='post_compra'),
	
>>>>>>> fa98660b45de57019fe6f40d7e8f076bce546715
)