from django.urls import include, path
from django.views.generic import RedirectView
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]

# urlpatterns += [
#     path('', RedirectView.as_view(url='/catalog/', permanent=True)),
# ]
