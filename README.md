<h1>The Wiki</h1>

بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيم


<p>This idea stemmed from <a href="https://github.com/justdjango">JustDjango's</a> basic boilerplate. I plan to build off of it and hopefully create something new or improved.</p>

<p>This is broken down into 2 sections - Core & Demo. Core will contain scripts that pertain to development, while Demo will contain the web app & it's information.</p>



<h3>Bugs/Problems & Solutions</h3>
#Notes::20191226

ERROR: django.contrib.sites.models.Site.DoesNotExist: Site matching query does not 
exist.

Resolution:
./manage.py shell

Type the following lines to resolve this error:

from django.contrib.sites.models import Site

site = Site.objects.create(domain='127.0.0.1', name='test')

site.save()

quit()


