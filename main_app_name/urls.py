from django.urls import path

from .views import base_views

urlpatterns = [
    # /views/base_views
    path("", base_views.pingpong_multi_method_acceptor, name="pingpong_multi_method_acceptor"),
    path("spec", base_views.spec, name="spec"),
]
