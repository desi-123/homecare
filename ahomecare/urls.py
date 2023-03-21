from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('testimonials/', include('testimonials.urls')),
    path('askedquestion/', include('askedquestion.urls')),
    path('blog/', include('blog.urls')),
    path('services/', include('services.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
