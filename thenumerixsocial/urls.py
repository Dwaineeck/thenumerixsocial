"""
URL configuration for thenumerixsocial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from courses import views as courses_views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', courses_views.home, name='home'),
    path('signup/', courses_views.signup, name='signup'),
    path('login/', courses_views.login_view, name='login'),
    path('logout/', courses_views.logout_view, name='logout'),
    path('notebook/<int:notebook_id>/', courses_views.notebook_detail, name='notebook_detail'),
    path('section/<int:section_id>/', courses_views.section_detail, name='section_detail')
]
