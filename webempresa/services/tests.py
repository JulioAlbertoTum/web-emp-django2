from django.test import TestCase

# Create your tests here.
def services(request):
    return render(request, "services/services.html")