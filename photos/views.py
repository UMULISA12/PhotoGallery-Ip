# from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
# from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Image,Location,Category

# Create your views here.
def welcome(request):
    images = Image.get_all_images()
    locations = Location.objects.all()

    return render(request, 'welcome.html', {'images':images, 'locations':locations})


def one_photo(request, category_name, image_id):
   

    locations = Location.objects.all()

    photo = Image.get_one_image(image_id)
    
    return render(request,'photo.html',{'image':image, 'image_category':image_category, 'locations':locations})


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day




# View Function to present news from past days
def past_days_photos(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

    return render(request, 'all-photos/past-photos.html', {"date": date})



def search_results(request):
    
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_images = Image.search_by_title(search_term)
        # message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

# def welcome(request):
   
#     images = Image.get_all_images()
#     locations = Location.objects.all()

#     return render(request, 'welcome.html', {images':images, 'locations':locations})

# def single_image(request, category_name, image_id):
   

#     locations = Location.objects.all()

#     image = Image.get_image_by_id(image_id)
    

#     image_category = Image.objects.filter(category__photo_category = category_name)
#     title = f'{category_name}'
#     return render(request,'single_image.html',{'title':title, 'image':image, 'image_category':image_category, 'locations':locations})

# def location_filter(request, location):
#     locations = Location.objects.all()
#     images = Image.filter_by_location(location)
#     title = f'{location} Photos'
#     return render(request, 'location.html', {'title':title, 'images':images, 'locations':locations})

# def search(request):
#     locations = Location.objects.all()
#     if 'category' in request.GET and request.GET['category']:
#         search_term = request.GET.get('category')
#         images_found = Image.search_image(search_term)
#         message = f'{search_term}'


#         return render(request, 'search.html',{'message':message, 'images':images_found, 'locations':locations})
#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{'message':message, 'locations':locations})