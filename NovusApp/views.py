from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

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

def onlineorder(request):
    return render(request, "onlineorder.html")

def VendorLanding(request):
    return render(request, "VendorLanding.html")

def calculate_sum(request):
    if request.method == 'POST':
        try:
            # Get values from the form submission
            latitude = float(request.POST.get('latitude', '0'))
            longitude = float(request.POST.get('longitude', '0'))

            # Calculate the sum
            def enzolocation(x,y):
                if (x-12.972576272433912)**2+(y-79.15886082535462)**2<0.00000625:
                    with open('user_input.txt', 'a') as file:
                        file.write("you can take a delivery from enzo"+ '\n')
                
            def quickbiteslocation(x,y):
                if (x-12.972907622362047)**2+(y-79.16392388302653)**2<0.00000625:
                    with open('user_input.txt', 'a') as file:
                        file.write("you can take a delivery from quickbites"+ '\n')

            def darlingcanteenlocation(x,y):
                if (x-12.970166973144979)**2+(y-79.15915036953444)**2<0.00000625:
                    with open('user_input.txt', 'a') as file:
                        file.write("you can take a delivery from darlingcanteen"+ '\n')

            def foodcourtlocation(x,y):
                if (x-12.97208852655021)**2+(y-79.1582451087028)**2<0.00000625:
                    with open('user_input.txt', 'a') as file:
                        file.write("you can take a delivery from foodcourt"+ '\n')

            def dcbakerylocation(x,y):
                if (x-12.97208852655021)**2+(y-79.1582451087028)**2<0.00000625:
                    with open('user_input.txt', 'a') as file:
                        file.write("you can take a delivery from DCBake"+ '\n')


            def arasanlocation(x,y):
                if (x-12.970977483068195)**2+(y-79.164430796518668)**2<0.00000625:
                    with open('user_input.txt', 'a') as file:
                        file.write("you can take a delivery from Arasan"+ '\n')

            def onefoodworldlocation(x,y):
                if (x-12.97284306739387)**2+(y-79.15702259837042)**2<0.00000625:
                    with open('user_input.txt', 'a') as file:
                        file.write("you can take a delivery from OneFoodWorld"+ '\n')

            def hangsandswigslocation(x,y):
                if (x-12.971850418564438)**2+(y-79.16468193884667)**2<0.00000625:
                    with open('user_input.txt', 'a') as file:
                        file.write("you can take a delivery from Hangs N Swigs"+ '\n')

            def main():
                x=latitude
                y=longitude
                enzolocation(x,y)
                quickbiteslocation(x,y)
                darlingcanteenlocation(x,y)
                foodcourtlocation(x,y)
                dcbakerylocation(x,y)
                arasanlocation(x,y)
                onefoodworldlocation(x,y)
                hangsandswigslocation(x,y)

            main()
            #12.969970314201683, 79.1557290406984 - anna auditorium
            #12.970877892592355, 79.15951637025026 - technology tower
            total = latitude + longitude

            # Convert the sum to a string
            result = str(total)

            return render(request, 'sum_result.html', {'result': result})

        except ValueError:
            return HttpResponse("Invalid input. Please enter valid numbers.")

    return render(request, 'calculate_sum.html')

def save_input_to_txt(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')

        # Save the input to a .txt file
        with open('user_input.txt', 'a') as file:
            file.write(query + '\n')

        return HttpResponse("Input saved successfully.")
    else:
        return HttpResponse("Invalid request method.")


def dbms(request):
    if request.method == 'POST':
        # Get the input data from the form submission
        input_text = request.POST.get('query', '')
        
        # Function to count vowels
        def check_food_in_restaurant(text):
            print('yes')
        # Count the number of vowels in the input text
        PossibleRestaurants = check_food_in_restaurant(input_text)
        
        # Return the result as an HTTP response
        return HttpResponse(f'Number of vowels in the input: {PossibleRestaurants}')

    return render(request, 'integrate.html')


# Create your views here.
