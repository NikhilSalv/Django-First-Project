from django.shortcuts import render

# Create your views here.

def index(request):
    meetups = [
        {
            'title':'A First Meetup',
            'location':'New York',
            'slug':'a-first-meetup'
        },
        {'title':'A Second Meetup',
        'location':'Paris',
        'slug':'a-second-meetup'
        }
    ]
    return render(request, 'meetups/index.html',{
        'show_meetups':True,
        'meetups': meetups
    })

def meetup_details(request):
    selected_meetup = {
        'title':'A First Meetup',
    'description': 'This is the First meetup!'
    }
    return render(render,'meetups/meetup-details.html',{
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })