from django.contrib.sitemaps import Sitemap
from info.models import Project, Information, Competence, Experience


class ProjectSitemap(Sitemap):
    def items(self):
        return Project.objects.all()


class InformationSitemap(Sitemap):
    def items(self):
        return Information.objects.all()


class CompetenceSitemap(Sitemap):
    def items(self):
        return Competence.objects.all()


class ExperienceSitemap(Sitemap):
    def items(self):
        return Experience.objects.all()