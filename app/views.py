import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from app.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    path = BUS_STATION_CSV
    with open(file=path, mode='r', newline='', encoding='utf-8', errors='replace') as csvfile:
        reader = csv.DictReader(csvfile)
        all_bus_stations = []
        for row in reader:
            all_bus_stations.append({
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            })

    page_number = request.GET.get("page", 1)
    paginator = Paginator(all_bus_stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'index.html', context)
