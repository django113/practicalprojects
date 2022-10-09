from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/', include('ADMIN.urls')),
    path('api/account/', include('ACCOUNT.urls')),
    path('api/auth/', include('AUTH.urls')),
    path('api/staff/', include('STAFF.urls')),
    path('api/product/', include('PRODUCT.urls')),
    path('api/delivery/', include('DELIVERY.urls')),
    path('api/order/', include('ORDER.urls')),
    path('api/logistic/', include('LOGISTIC.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
