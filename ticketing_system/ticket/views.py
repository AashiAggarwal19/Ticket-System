from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ticket
import datetime
from .form import CreateTicketForm, UpdateTicketForm

#view ticket details
def ticket_details(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    context = {'tickets': ticket}
    return render(request,'ticket/ticket_details.html',context)



"""FOR CUSTOMERS"""
# creating a ticket

def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit = False)
            var.created_by = request.user
            var.ticket_status = 'Pending'
            var.save()
            messages.info(request, "Your ticket has been successfully submitted. An engineer would be assigned soon")
            return redirect('dashboard')
        
        else:
            messages.warning(request, 'Something went Wrong.')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm()
        context = {'form': form}
        return render(request, 'ticket/create_ticket.html', context)
    
#updating the ticket
def update_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateTicketForm(request.POST, instance=ticket)
        if form.is_valid():
           form.save()
           messages.info(request, "Your ticket info has been updated and all the changes are saved in the database")
           return redirect('dashboard')
        
        else:
            messages.warning(request, 'Something went Wrong.')
    else:
        form = UpdateTicketForm(instance=ticket)
        context = {'form': form}
        return render(request, 'ticket/update_ticket.html', context)

#viewing all tickets
def all_tickets(request):
    tickets = Ticket.objects.filter(created_by = request.user)
    context = {'tickets': tickets}
    return render(request, 'ticket/all_tickets.html', context)

"""For Engineers"""

#view ticket queue
def ticket_queue(request):
    tickets = Ticket.objects.filter(ticket_status ='Pending')
    context = {'tickets': tickets}
    return render(request, 'ticket/tickets_queue.html', context)

#accept a ticket from the queue
def accept_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.assigned_to = request.user
    ticket.ticket_status = 'Active'
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket has been accepted!!')
    return redirect('ticket-queue')
#close a ticket from the queue
def close_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.assigned_to = request.user
    ticket.ticket_status = 'Completed'
    ticket.is_resolved

    ticket.closed_date = datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket has been resolved!! Thankyou.')
    return redirect('ticket-queue')

#ticket engineer is working on
def workspace(request):
    tickets = Ticket.objects.filter(assigned_to=request.user, is_resolved= False)
    context = {'tickets': tickets}
    return render(request,'ticket/workspace.html', context)

#all closed and resolved tickets
def all_closed_tickets(request):
    tickets = Ticket.objects.filter(assigned_to= request.user, is_resolved = True)
    context = {'tickets': tickets}
    return render(request, 'ticket/all_closed_tickets.html', context)







 





    





        