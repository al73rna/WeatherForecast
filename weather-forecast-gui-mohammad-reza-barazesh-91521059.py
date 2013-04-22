import re
import urllib2
import gtk
##==================================##

cities = {"tehran":"IRXX0018","tabriz":'IRXX0016',"kermanshah":"IRXX0029" , "esfahan":"IRXX0003" , "mashhad":"IRXX0008","shiraz":"IRXX0015",}


class mainform :
    def __init__(self):
        
        self.builder = gtk.Builder()
        self.builder.add_from_file("wtr.glade")
        self.window = self.builder.get_object("window1")
        self.builder.connect_signals(self)
        self.entry = self.builder.get_object("entry1")
        self.tmrow = self.builder.get_object("label4")
        self.tday = self.builder.get_object("label3")


    def on_button1_clicked(self,widget) :
        self.entered_city = self.entry.get_text()
        self.pattern = re.compile(r"""<img src="(.+)" height="70" width="70" alt="(.+)" class="wx-weather-icon">""")
        self.site = urllib2.urlopen('http://www.weather.com//weather//tenday//'+cities[self.entered_city])
        self.Weather_now = self.pattern.findall(self.site.read())
        self.tday.set_text(self.Weather_now[0][1])
        self.tmrow.set_text(self.Weather_now[1][1])

newform = mainform()
newform.window.show()
gtk.mainloop()








