from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { "my_list":
    [
    { 
    "restaurant_name": " aaa",
    "food_type" : "Buttered toas ",

    },
    { 
    "restaurant_name": " bbb",
    "food_type" : "  Corn ",

    },
    { 
    "restaurant_name": " ccc",
    "food_type" : " Hamburger" ,

    },



    ]


    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { "my_object":
     { 
    "restaurant_name": " ccc",
    "food_type" : "Hamburger ",

    },
    


    }
    return render(request, 'detail.html', context)
