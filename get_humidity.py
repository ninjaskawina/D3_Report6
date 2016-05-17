import urllib.request
import xml.etree.ElementTree as ET

response = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Cracow&APPID=62c813137a6c5df7bd8f031400c0102c&mode=xml&units=metric").read()
current = ET.fromstring(response)
temp1 = current[2].attrib['value']
response = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Warszawa%20Angeles&APPID=62c813137a6c5df7bd8f031400c0102c&mode=xml&units=metric").read()
current = ET.fromstring(response)
temp2 = current[2].attrib['value']
response = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Poznan&APPID=62c813137a6c5df7bd8f031400c0102c&mode=xml&units=metric").read()
current = ET.fromstring(response)
temp3 = current[2].attrib['value']


print("{\n\t\"temp1\": \"" + temp1 + "\",\n")
print("\t\"temp2\": \"" + temp2 + "\",\n")
print("\t\"temp3\": \"" + temp3 + "\"\n")
print("}")
