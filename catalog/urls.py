from django.urls import include, path

urlpatterns += [
     path('catalog/', include('catalog.urls')),
]
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]