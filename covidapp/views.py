from django.shortcuts import render
from matplotlib.style import context
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "8ddaa28a6cmshf2ca4ad91d1aef1p1059c4jsnda90022d84f4"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def helloworldview(request):
  mylist = []
  noofresults = int(response['results'])
  for x in range(0,noofresults):
    mylist.append(response['response'][x]['country'])
    mylist.sort()
  if request.method == "POST":
    selectedcountry = request.POST['selectedcountry']
    noofresults = int(response['results'])
    for x in range(0,noofresults):
      if selectedcountry==response['response'][x]['country']:
        new = response['response'][x]['cases']['new']
        active = response['response'][x]['cases']['active']
        critical = response['response'][x]['cases']['critical']
        recovered = response['response'][x]['cases']['recovered']
        total = response['response'][x]['cases']['total']
        deaths = int(total)-int(active)-int(recovered)
    context = {'selectedcountry':selectedcountry,'mylist': mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'deaths':deaths,'total':total}
    return render(request,'helloworld.html',context)
  
  context = {'mylist': mylist }
  return render(request,'helloworld.html',context)