from django.shortcuts import render

# import folium

# map = folium.Map(location=[32.401867, -111.112322]) # pust = 24.0131° N, 89.2797° E
# map.save('map.html')


from .forms import  Examformfillup

def showformdata(request):
    if request.method == 'POST':
        fm = Examformfillup(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['studentid']
            em = fm.cleaned_data['name']
            pw = fm.cleaned_data['email']
            qw = fm.cleaned_data['password']
            print(nm)
            print(em)
            print(pw)
            print(qw)
    else:
        fm = Examformfillup()
    return render(request, 'ExamFormFillUp/ExamForm.html', {'form': fm})
