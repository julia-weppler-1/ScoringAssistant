# excel_app/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExcelUploadForm
import pandas as pd
import copy

def process_excel_file(excel_file):
    df = pd.read_excel(excel_file, sheet_name='Sheet1')
    data = df.set_index('GYMNAST').T.to_dict('list')
    return data
def download_template(request):
    # Load your Excel template file
    with open('./excel_app/static/MeetTemplate.xlsx', 'rb') as f:
        template_data = f.read()
    # Prepare response with the Excel template file as attachment
    response = HttpResponse(template_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="template.xlsx"'
    return response
def level_filter(data):
    lvl = {}
    for x in data:
        if data[x][1] not in lvl:
            b = copy.deepcopy(data[x])
            data[x].remove(data[x][1])
            lvl[b[1]] = [[x, data[x]]]
        else:
            b = copy.deepcopy(data[x])
            data[x].remove(data[x][1])
            lvl[b[1]] += [[x, data[x]]]
    return lvl

def vault(lst):
    vault_scores = {}
    for gymnast in lst:
        vault_scores[gymnast[0]] = gymnast[1][1]
    return dict(sorted(vault_scores.items(), key=lambda item: item[1], reverse=True))

def bars(lst):
    bar_scores = {}
    for gymnast in lst:
        bar_scores[gymnast[0]] = gymnast[1][2]
    return dict(sorted(bar_scores.items(), key=lambda item: item[1], reverse=True))

def beam(lst):
    beam_scores = {}
    for gymnast in lst:
        beam_scores[gymnast[0]] = gymnast[1][3]
    return dict(sorted(beam_scores.items(), key=lambda item: item[1], reverse=True))

def floor(lst):
    floor_scores = {}
    for gymnast in lst:
        floor_scores[gymnast[0]] = gymnast[1][4]
    return dict(sorted(floor_scores.items(), key=lambda item: item[1], reverse=True))

def all_around(lst):
    aa = {}
    for gymnast in lst:
        # Convert scores to floats before summing
        scores = [float(score) for score in gymnast[1][1:5]]  # Convert each score to float
        print(scores)
        total = round(sum(scores), 2)  # Sum up the converted scores
        aa[gymnast[0]] = total
    return dict(sorted(aa.items(), key=lambda item: item[1], reverse=True))



def generate_results_file(data):
    result_text = ""
    for level, gymnasts in data.items():
        result_text += f"Level: {level}\n\n"
        
        # Generate results for each event
        events = {
            "Vault": vault,
            "Bars": bars,
            "Beam": beam,
            "Floor": floor,
            "All-Around": all_around
        }
        
        for event_name, event_func in events.items():
            result_text += f"{event_name}\n"
            sorted_results = sorted(event_func(gymnasts).items(), key=lambda x: x[1], reverse=True)
            result_text += generate_event_result_text(sorted_results)
        
        result_text += "\n\n"

    return result_text

def generate_event_result_text(sorted_results):
    result_text = ""
    result_dict = {}  # Dictionary to store scores as keys and list of gymnasts as values
    for gymnast, score in sorted_results:
        if score not in result_dict:
            result_dict[score] = [gymnast]
        else:
            result_dict[score].append(gymnast)
    
    i = 1
    for score, gymnasts in result_dict.items():
        if len(gymnasts) == 1:
            result_text += f"{i}: {gymnasts[0]}: {score}\n"
        else:
            names_str = ' / '.join(gymnasts)
            result_text += f"{i}: TIE - {names_str}: {score}\n"
        i += len(gymnasts)
        
    return result_text



def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            data = process_excel_file(excel_file)
            data = level_filter(data)
            result_text = generate_results_file(data)  # Call the modified function
            response = HttpResponse(result_text, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="results.txt"'
            return response
    else:
        form = ExcelUploadForm()
    return render(request, 'upload.html', {'form': form})
