from django.views.generic import ListView

from .models import Build


class BuildListView(ListView):
    model = Build
    paginate_by = 2
