from boaapp import views as boaapp_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('upload/progress/', boaapp_views.upload_progress, name='upload_progress'),
    path('admin/', admin.site.urls),
    path('register/', boaapp_views.register, name='register'),
    path('login/', boaapp_views.login_view, name='login'),
    path('logout/', boaapp_views.logout_view, name='logout'),
    path('', boaapp_views.home, name='home'),
    path('upload/', boaapp_views.upload_document, name='upload_document'),
    path('upload/success/', boaapp_views.upload_success, name='upload_success'),
    path('starburst-data/', boaapp_views.starburst_data_view, name='starburst_data'),

]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
