from django.conf.urls.defaults import *
from django.views.generic import ListView
from team.models import Member

def team_list(team_name=None):
	if team_name is None:
		queryset = Member.objects.all()
	else:
		queryset = Member.objects.filter(name=team_name)
		
	urlpatterns = patterns('',
		(r'^/$', ListView.as_view(
		    queryset=queryset,
		    context_object_name="member_list",
		)),
	)
	
	return urlpatterns

urlpatterns = team_list()
