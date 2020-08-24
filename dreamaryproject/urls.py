
from django.contrib import admin
from django.urls import path, include
from page import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('introduce/',views.introduce, name="introduce"),
    path('new/',views.new, name="new"),
    path('create/',views.create, name="create"),
    path('delete/<int:designer_id>/',views.delete, name="delete")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
