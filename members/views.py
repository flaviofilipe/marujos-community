from django.shortcuts import render
from members.models import Member

def members(request):
	members = list( Member.objects.all().values() )

	context = {
		'members': []
	}

	for i in range(len(members)):
		print(members[i]['avatar'])
		context['members'].append(
			{
				'name': members[i]['name'],
				'avatar': members[i]['avatar'],
				'job': members[i]['job'],
				'resume': members[i]['resume']
			}
		)

	return render(request, 'members/members.html', context)