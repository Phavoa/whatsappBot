import csv
from django.shortcuts import render


def read_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        csv_data = []
        # Read the CSV file
        csv_reader = csv.reader(csv_file.read().decode('utf-8').splitlines())
        for row in csv_reader:
            csv_data.append(row)
        return render(request, 'csv_view.html', {'csv_data': csv_data})
    return render(request, 'upload_csv.html')

def campaign(request):
    return render(request, 'campaign.html')
