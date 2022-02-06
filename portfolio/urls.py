from django.contrib import admin
from django.urls import path, include
from .views import (
    homePage,
    projectsPage,
    projectDetail,
    search,
    handler404,
)

from django.views.static import serve
from django.conf.urls import  url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from portfolio.sitemaps import *


sitemaps = {
    "Project":ProjectSitemap,
    "Information":InformationSitemap,
    "Competence":CompetenceSitemap,
    "Experience":ExperienceSitemap
}

handler404 = handler404

urlpatterns = [

    path('', homePage, name='homePage'),
    path('projects/', projectsPage, name='projectsPage'),
    path('projects/<str:slug>/', projectDetail, name='projectDetail'),
    path('search/', search, name='search'),

    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('sitemap.xml', sitemap, {"sitemaps":sitemaps})

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
