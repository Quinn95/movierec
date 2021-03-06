from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from useraccount.views import SignupView

#changed

urlpatterns = [
    url(r"^", include('movierec.urls'), name="homepage"),
    url(r"^admin/", include(admin.site.urls)),
    url(r'^profile/', include('useraccount.urls')),
    url(r"^account/signup/$", SignupView.as_view(), name="account_signup"),
    url(r'^account/', include('account.urls')),
    #url(r'^movierec/', include('movierec.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
