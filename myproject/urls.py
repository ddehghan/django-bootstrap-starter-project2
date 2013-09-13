from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from myproject import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

                       url(r'^$', 'website.views.index', name='index'),
                       url(r'^login-forms', 'website.views.login_test', name='login_test'),
                       url(r'^private', 'website.views.private', name='private'),

                       # url("^index", TemplateView.as_view(template_name='index.html'), name="mission"),

                       # Admin site
                       #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       # Server Static Files from Django
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),

                       # Social Auth:
                       url('', include('social.apps.django_app.urls', namespace='social')),

                       url("^robots\.txt", TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),
                           name="robots"),
)