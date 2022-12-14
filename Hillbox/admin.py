from django.contrib import admin

# i learned admin from ci blod walkthrough
# Register your models here.
from django.contrib import admin
from .models import FlyingSite, Comment, Photo, PhotoComment

# this is the admin for the FlyingSite 
@admin.register(FlyingSite)
class FlyingSiteAdmin(admin.ModelAdmin):
    actions = ['approve_sites']
    list_display = ('site_name', 'updated_on', 'approved', 'pilot')
    search_fields = ['site_name', 'wind_direction']
    list_filter = ('approved', 'updated_on')


    def approve_flying_sites(self, request, queryset):
        queryset.update(approved = True)

# this id the admin for the gallery images / photos
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    actions = ['approve_photos']
    list_display = ('site_name', 'updated_on', 'approved')
    search_fields = ['site_name', 'wind_direction']
    list_filter = ('approved', 'updated_on')


    def approve_photos(self, request, queryset):
        queryset.update(approved = True)

# this admin is for the flying site comments
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    actions = ['approve_comments']
    list_display = ('site', 'created_on', 'approved', 'name')
    list_filter = ('approved', 'created_on')
    search_fields = ['site', 'name']


    def approve_comments(self, request, queryset):
        queryset.update(approved = True)

# this is the photo comment admin
@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    actions = ['approve_comments']
    list_display = ('photo', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['photo', 'name']


    def approve_comments(self, request, queryset):
        queryset.update(approved = True)