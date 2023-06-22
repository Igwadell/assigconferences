from django.shortcuts import render

def conference_list(request):
    conferences = [
        {'id': 1, 'title': 'Conference 1', 'date': '2023-07-01', 'location': 'City 1'},
        {'id': 2, 'title': 'Conference 2', 'date': '2023-08-15', 'location': 'City 2'},
        {'id': 3, 'title': 'Conference 3', 'date': '2023-09-30', 'location': 'City 3'},
    ]
    context = {'conferences': conferences}
    return render(request, 'conferences/conference_list.html', context)

def conference_create(request):
    return render(request, 'conferences/conference_create.html')

def conference_details(request, conference_id):
    conference = {
        'id': conference_id,
        'title': 'Conference {}'.format(conference_id),
        'date': '2023-07-01',
        'location': 'City {}'.format(conference_id),
    }
    context = {'conference': conference}
    return render(request, 'conferences/conference_details.html', context)

def conference_update(request, conference_id):
    conference = {
        'id': conference_id,
        'title': 'Conference {}'.format(conference_id),
        'date': '2023-07-01',
        'location': 'City {}'.format(conference_id),
    }
    context = {'conference': conference}
    return render(request, 'conferences/conference_update.html', context)

def conference_delete(request, conference_id):
    conference = {
        'id': conference_id,
        'title': 'Conference {}'.format(conference_id),
        'date': '2023-07-01',
        'location': 'City {}'.format(conference_id),
    }
    context = {'conference': conference}
    return render(request, 'conferences/conference_delete.html', context)
