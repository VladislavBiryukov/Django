import mainapp.views as mainapp


urlpatterns = [
    re_path(r"^$", mainapp.main, name="main"),
    re_path(r"^products/", include("mainapp.urls", namespace="products")),
    re_path(r"^contact/", mainapp.contact, name="contact"),

    re_path(r"^admin/", include("adminapp.urls", namespace="admin")),
]


if settings.DEBUG:

