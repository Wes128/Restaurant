from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from application.forms import ReservationForm
from application.models import Reservation


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')

def event(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event')
    else:
        form = ReservationForm()
    return render(request, 'event.html', {'form':form})
    # return render(request,'event.html')

def gallery(request):
    return render(request,'gallery.html')

# def booking(request):
#     return render(request,'booking.html')

def chef(request):
    return render(request,'chef.html')

def contact(request):
    return render(request,'contact.html')

# def create_reservation(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form.save()
#             return redirect(request, '')
#     else:
#         form = ReservationForm()
#     return render(request, 'event.html', {'form':form})

def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            return render(request, 'event.html', {'form': form, 'success': True})
    else:
        form = ReservationForm()
    return render(request, 'event.html', {'form': form})

def booking(request):
    reservations = Reservation.objects.all()
    return render(request, 'booking.html', {'reservations': reservations})

def update(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully!")
            return redirect('booking')
    else:
        form = ReservationForm(instance=reservation)
        messages.error(request, 'Please confirm your changes')
    return render(request, 'update.html', {'form': form})

def delete(request,id):
    reservation = get_object_or_404(Reservation,id=id)

    try:
        reservation.delete()
        messages.success(request, 'Customer deleted successfully')
    except Exception as e:
        messages.error(request, 'Customer not deleted')
    return redirect('booking')
