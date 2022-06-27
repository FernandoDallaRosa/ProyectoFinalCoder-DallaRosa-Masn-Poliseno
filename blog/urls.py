from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("crear/", views.BlogCreate.as_view(), name="blog_create"),
    path("detalle/<pk>/", views.PostDetail.as_view(), name ="blog_detail"),
    path("editar/<pk>/", views.BlogUpdate.as_view(), name ="blog_update"),
    path("borrar/<pk>/", views.BlogDelete.as_view(), name ="blog_delete"),
    path("entrar/", views.BlogLogin.as_view(), name="blog_login"),
    path("salir/", views.BlogLogout.as_view(), name="blog_logout"),
    path("about/", views.About.as_view(), name="about"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)