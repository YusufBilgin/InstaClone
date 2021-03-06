from django.urls import path
from post import views

app_name = "post"

urlpatterns = [
    path('ayrıntı/<int:id>/', views.detail, name = "detail"),
    path('beğen/<int:post_id>/', views.like, name = "like"),
    path('arşive-kaydet/<int:post_id>/', views.save_post_to_archive, name = "savePostToArchive"),
    path('yorum-yap/<int:id>/<str:redirectTo>/', views.addComment, name = "addComment"),
    # path('sil/<int:id>/', views.delete_post, name = "deletePost"),
]