from django.conf.urls.defaults import *
from django.views.generic import ListView
from team.models import Member

def team_list(*teams):
	if teams:
		queryset = Member.objects.filter(teams__name__in=teams)
	else:
		queryset = Member.objects.all()
		
	urlpatterns = patterns('',
		(r'^/$', ListView.as_view(
		    queryset=queryset,
		    context_object_name="member_list",
		)),
	)
	
	return urlpatterns

urlpatterns = team_list()
