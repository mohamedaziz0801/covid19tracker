from django.shortcuts import render
from django.http import HttpResponse 
from covid import Covid
from django.utils.datastructures import MultiValueDictKeyError

'''covid=Covid()
#ui=str(input("\nEnter country name :  "))



countryname = covid.get_status_by_country_name('italy')
data={

    key:countryname[key]
    for key in countryname.keys() and {'confirmed',
    'active',
    'recovered',
    'deaths'}
    
}
s=list(data.values())

content={'t1':s[0],'t2':s[1],'t3':s[2],'t4':s[3]}'''
def covidtest(request):
    
    #a=request.POST["country"]
    try:
        a = request.POST['country']
    except MultiValueDictKeyError:
        a = 'italy'
    covid=Covid()
    name = covid.get_status_by_country_name(str(a))
    data={

        key:name[key]
        for key in name.keys() and {'confirmed',
        'active',
        'recovered',
        'deaths'}
        
    }
    s=list(data.values())
    p1=str(int((s[1]/s[0])*100))+'%'
    p2=str(int((s[2]/s[0])*100))+'%'
    p3=str(int((s[3]/s[0])*100))+'%'

    content={'t1':s[0],'t2':s[1],'t3':s[2],'t4':s[3]}
    percent={'p1':p1,'p2':p2,'p3':p3}
    
    return render(request, 'index.html' , { 'd1':content , 'd2':percent} )
    

