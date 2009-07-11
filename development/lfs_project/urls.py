from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import os
DIRNAME = os.path.dirname(__file__)

handler500 = 'lfs.core.views.server_error'

urlpatterns = patterns("",    
    (r'^reviews/', include('reviews.urls')),
    (r'^paypal/ipn/', include('paypal.standard.ipn.urls')),
    (r'^paypal/pdt/', include('paypal.standard.pdt.urls')),    
)

urlpatterns += patterns("",    
    (r'^admin/(.*)', admin.site.root),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(DIRNAME, "media"), 'show_indexes': True }),
)

urlpatterns += patterns("",    
   (r'^dh/', include('demmelhuber.urls')),
)

urlpatterns += patterns("",
    url(r'^contact$', "contact_form.views.contact_form", name='contact_form'),
)

urlpatterns += patterns("",
    (r'^manage/', include('lfs.manage.urls')),
    (r'^shop/', include('demmelhuber_theme.urls')),
)