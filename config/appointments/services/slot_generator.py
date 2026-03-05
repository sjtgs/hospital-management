from datetime import datetime, timedelta, time

from appointments.models import Appointment
from appointments.services.scheduling_engine import APPOINTMENT_DURATION



def generate_available_slots(doctor, appointment_date):
    """
    Generate all available appointment slots for a doctor
    based on working hours and existing appointments.
    """

    slots = []

    start_time = doctor.work_start_time
    end_time = doctor.work_end_time

    current_slot = datetime.combine(appointment_date, start_time)
    end_datetime = datetime.combine(appointment_date, end_time)

    # Existing booked appointments
    booked_times = Appointment.objects.filter(
        doctor=doctor,
        appointment_date=appointment_date
    ).values_list("appointment_time", flat=True)

    while current_slot + APPOINTMENT_DURATION <= end_datetime:

        slot_time = current_slot.time()

        if slot_time not in booked_times:
            slots.append(slot_time)

        current_slot += APPOINTMENT_DURATION

    return slots