from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def supp(request):
    return render(request, "supp.html")

def register(request):
    return render(request, "register.html")

def reviews(request):
    return render(request, "reviews.html")

def arsan(request):
    return render(request, "arsan.html")

def buddys(request):
    return render(request, "buddys.html")

def cafe(request):
    return render(request, "cafe.html")

def canteen(request):
    return render(request, "canteen.html")

def enzo(request):
    return render(request, "enzo.html")

def foodcourt(request):
    return render(request, "foodcourt.html")

def hns(request):
    return render(request, "hns.html")

def onefood(request):
    return render(request, "onefood.html")

def quickbites(request):
    return render(request, "quickbites.html")

def save_input_to_txt(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')

        # Save the input to a .txt file
        with open('user_input.txt', 'a') as file:
            file.write(query + '\n')

        return HttpResponse("Input saved successfully.")
    else:
        return HttpResponse("Invalid request method.")





# Create your views here.
