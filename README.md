<h1>Rough Draft Project - The Wiki</h1>

بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيم


<p>Credit goes where credit is due, this stemmed from <a href="https://github.com/justdjango">JustDjango's</a> basic boilerplate. </p>

<p>The original purpose of this project was to provide a staus, user-changeable, display of current software versions of a particular product. The eventual goal is to be an out of the box, easy to install, application. The following have been added:</p>
<ul>
  <li> Color coded software version!</li>
  <li> User registration</li>
  <li> Demo: HowTo Flatpage</li>
  <li> Status page </li>
  <li> and more...</li>
</ul>     


<h3>Side notes and blues:</h3>
ERROR: django.contrib.sites.models.Site.DoesNotExist: Site matching query does not 
exist.

Resolution:
./manage.py shell

Type the following lines to resolve this error:

from django.contrib.sites.models import Site

site = Site.objects.create(domain='127.0.0.1', name='test')

site.save()

quit()


