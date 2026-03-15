from django.shortcuts import render
from .services import get_doctor_queue

def doctor_queue(request):
    # Assuming `request.user.doctor_profile` exists
    doctor = request.user.doctor_profile

    queue = get_doctor_queue(doctor)

    context = {"queue": queue}
    return render(request, "appointments/doctor_queue.html", context)