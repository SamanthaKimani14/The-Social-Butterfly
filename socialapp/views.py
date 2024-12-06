from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .models import Event,RSVP
from .forms import RegistrationForm, EventForm, ContactMessageForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            return redirect('login')  # Redirect to login page after registration
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('event_list')  # Redirect to the event list after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to the event list after creating
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


def event_list(request):
    event_type = request.GET.get('type')
    if event_type:
        events = Event.objects.filter(event_type=event_type)
    else:
        events = Event.objects.all()

    return render(request, 'event_list.html', {'events': events})




def index(request):
    return render(request,'index.html')
def delete_event(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, id=event_id)
        event.delete()
        return redirect('event_list')
def home(request):
    return render(request,'main.html')
def rsvp_event(request, event_id):
    event = Event.objects.get(id=event_id)
    RSVP.objects.create(event=event, attendee=request.user)
    return redirect('event_list')

def children(request):
    return render(request,'children.html')

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactMessageForm()

    return render(request, 'contact.html', {'form': form})

def corporate(request):
    return render(request,'corporate.html')

def entertainment(request):
    return render(request,'entertainment.html')

def peer(request):
    return render(request,'peer.html')

def teen(request):
    return render(request,'teen.html')

def event_list_view(request):
    events = Event.objects.all()  # Fetch all events from the database
    return render(request, 'event_list.html', {'events': events})














