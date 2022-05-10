from django.urls import path
from . import views
urlpatterns = [
    path('test',views.test),
    path('add-item',views.add_item),
    path('list-items', views.list_item), # [{"item":"orange", "description"}]
    path('delete-item/<id>',views.delete_item ),
    path("update-item/<id>",views.update_item ), # {"item":"sas", "desc":"wqe"}
]
