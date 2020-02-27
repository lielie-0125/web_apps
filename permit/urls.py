from django.urls import path

from . import views

app_name = "permit"

urlpatterns = [
    # 负责业务逻辑的视图
    path("", views.index, name="index"),
    path("submit", views.submit, name="submit"),
    path("success/<int:id_number>", views.success, name="success"),
    path("detail/<int:id_number>", views.detail, name="detail"),

    # ajax视图，这里不能加 name 选项，否则在使用 {% url 'url' %} 标签的时候回发生转换的错误
    path("area", views.get_area_data),
    path("success/site", views.get_site),
]
