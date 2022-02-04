
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import ListView

from .forms import *
from .models import Category


def index(request):
    return render(request, "index.html")


class BuiltListView(ListView):
    paginate_by = 1
    model = Build
    template_name = 'gallery.html'
    context_object_name = 'obj'


def full_width(request):
    obj = Build.objects.all()
    return render(request, "full-width.html", locals())


def basic_grid(request):
    return render(request, "basic-grid.html")


def create_house(request):
    build_form = BuildingForm()
    image_form = UploadImageForm()

    if request.method == "POST":
        build_form = BuildingForm(request.POST)
        image_form = UploadImageForm(request.POST, request.FILES)

        if build_form.is_valid() and image_form.is_valid():
            build = build_form.save()

            image_object = Image.objects.create(
                image=image_form.cleaned_data["image"], building=build
            )
            image_object.save()

            return redirect(build.get_absolute_url())
        else:
            build_form = BuildingForm()
            image_form = UploadImageForm()

    return render(
        request,
        "create_house.html",
        {"build_form": build_form, "image_form": image_form},
    )


def update_build(request, pk):
    build = get_object_or_404(Build, pk=pk)
    image = get_object_or_404(Image, building=build)

    ImageFormSet = ImageForm(
        request.POST or None, request.FILES or None, instance=image
    )
    build_form = BuildingForm(request.POST or None, instance=build)

    if build_form.is_valid() and ImageFormSet.is_valid():
        build_form.save()
        ImageFormSet.save()
        return redirect(build.get_absolute_url())

    return render(
        request,
        "update_build.html",
        context={"image_form": ImageFormSet, "build_form": build_form},
    )


def delete_build(request, pk):
    product = get_object_or_404(Build, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('gallery')
    return render(request, 'delete_build.html', locals())


def about_us(request):
    return render(request, "about-us.html")


def bait_house(request):
    return render(request, 'baithouse-city.html')


def search_venues(request):
    if request.method == 'POST':
        searched = request.GET.get['q']
        venues = Category.objects.filter(name__contains=searched)

        return render(request, 'search_venues.html',{'searched': searched, 'venues': venues})
    else:
        return render(request, 'search_venues.html',{})


def spanish_house(request):
    return render(request, 'spanish-house.html')


def french_kvartal(request):
    return render(request, 'french.html')


class GalleryListView(ListView):
    # model = Build
    template_name = 'gallery.html'
    context_object_name = 'builds'
    paginate_by = 1


    def get_queryset(self):
        queryset = Build.objects.all()
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset

