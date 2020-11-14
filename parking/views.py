from django.http import HttpResponse

def home(request):
    return HttpResponse('parking home page')

def getSlotByCarNo(request):
    return HttpResponse('get Slot by Car Number')

def getCarNoBySlot(request):
    return HttpResponse('get Car number by Slot')
