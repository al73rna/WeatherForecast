import re
import urllib2
##===================
cities = {"tehran":"IRXX0018","tabriz":'IRXX0016',"kermanshah":"IRXX0029","esfahan":"IRXX0003","mashhad":"IRXX0008","shiraz":"IRXX0015",}
print "enter the name of the city u want to know the weather of ? "
entered_city = raw_input("city name :",)
if entered_city in cities.keys() :
    pattern = re.compile(r"""<img src="(.+)" height="70" width="70" alt="(.+)" class="wx-weather-icon">""")
    site = urllib2.urlopen('http://www.weather.com//weather//tenday//'+cities[entered_city])
    Weather_now =pattern.findall(site.read())
    print "The weather in",entered_city, "is "+ Weather_now[0][1]+" right now ."
    print "The weather in",entered_city, "is going to be "+Weather_now[1][1]+" tomorrow ."
else :
    print "INVALID CITY NAME "

raw_input("Press anykey to exit ...")