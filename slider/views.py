from django.shortcuts import render

from slider.models import Slider


def main(request):
    slider = Slider.objects.all()
    return render(
        request,
        'index.html',
        {
            'slider': slider,
        }
    )
