from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ParkingSlot
import json



def dashboard(request):
    slots = ParkingSlot.objects.all()

    return render(
        request,
        'dashboard.html',
        {
            'slots': slots
        }
    )


@csrf_exempt
def update_slot(request):

    if request.method == "POST":

        data = json.loads(request.body)

        for slot, status in data.items():

            slot_number = int(slot.replace("slot", ""))

            ParkingSlot.objects.update_or_create(
                slot_number=slot_number,
                defaults={
                    "status": status
                }
            )

        return JsonResponse({
            "message": "Parking status updated"
        })

    return JsonResponse({
        "message": "Only POST allowed"
    })
