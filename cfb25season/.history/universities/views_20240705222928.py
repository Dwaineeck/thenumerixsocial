# universities/views.py
import folium
from django.shortcuts import render

from .models import University


def university_map(request):
    universities = University.objects.all()
    map = folium.Map(location=[39.8283, -98.5795], zoom_start=5)

    for uni in universities:
        folium.Marker(
            [uni.latitude, uni.longitude], 
            popup=f"<b>{uni.name}</b><br><img src='{uni.logo_url}' height='50' width='50'>", 
            icon=folium.CustomIcon(icon_image=uni.logo_url, icon_size=(50, 50))
        ).add_to(map)

    map = map._repr_html_()
    return render(request, 'universities/map.html', {'map': map})
