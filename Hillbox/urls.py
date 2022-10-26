from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('not_authorised', views.NotAuthorised, name='not_authorised'),
    path('sites/', views.SiteList.as_view(), name='sites'),
    path('gallery/', views.PhotoList.as_view(), name='gallery'),
    path('gallery/<slug:slug>/', views.PhotoDetail.as_view(), name='photo_detail'),
    path('gallery_upload/', views.UploadGalleryImage, name='gallery_upload'),
    path('gallery/delete/<uploaded_by>/<photo_id>', views.DeleteGallery, name='delete_gallery'),
    path('edit/<site_id>', views.EditSite, name='edit'),
    path('delete/<site_id>', views.DeleteSite, name='delete'),
    path('sites/<slug:slug>/', views.SiteDetail.as_view(), name='site_detail'),
    path('site_comment_edit/<comment_id>', views.EditComment, name='site_comment_edit'),
    path('site_comment_delete/<comment_id>', views.DeleteComment, name='site_comment_delete'),
    
      
]