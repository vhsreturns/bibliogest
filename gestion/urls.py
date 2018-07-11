from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from gestion.views import LibrosList

urlpatterns = [
    path('', LibrosList.as_view(), name='listado_libros'),
    path('catalogo', LibrosList.as_view(), name="listado_libros"),
    path('catalogo/<int:pk>', views.confirmar_prestamo, name="detalle-prestamo"),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/deletePrestamo/<int:pk>', views.remove_prestamo_view, name='prestamo-delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)