from django.shortcuts import render

def conference_list(request):
    return render(request, 'conferences/conference_list.html')

def conference_create(request):
    return render(request, 'conferences/conference_create.html')

def conference_details(request, conference_id):
    return render(request, 'conferences/conference_details.html')

def conference_update(request, conference_id):
    return render(request, 'conferences/conference_update.html')

def conference_delete(request, conference_id):
    return render(request, 'conferences/conference_delete.html')
