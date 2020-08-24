from django.urls import path
from . import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',include('page.urls')),
    path('profile/<int:designer_id>',views.detail, name="detail"),
]