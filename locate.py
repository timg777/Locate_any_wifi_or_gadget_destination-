import requests
import sys
import xml.etree.ElementTree as ET
import webbrowser
import os
from termcolor import colored

if __name__ == '__main__':

    os.system('clear')

    while True:

        print(colored('choose:\t   [BSSID]   |   [MAC_ADDR]\n', 'red'))
        inp = input(colored('And text it! --> ', 'green'))

        try:

            url = 'http://mobile.maps.yandex.net/cellid_location/?clid=1866854&lac=-1&cellid=-1&operatorid=null&countrycode=null&signalstrength=-1&wifinetworks={}:-65&app=ymetro'
            BSSID = inp.upper().replace(':', '')

            xml_tree_response = ET.fromstring(requests.get(url.format(BSSID)).text)

            latitude = xml_tree_response[0].attrib['latitude']
            longitude = xml_tree_response[0].attrib['longitude']
            nlatitude = xml_tree_response[0].attrib['nlatitude']
            nlongitude = xml_tree_response[0].attrib['nlongitude']

            geocode = [latitude, longitude, nlatitude, nlongitude]

            webbrowser.open('https://www.google.com/maps/place/' + geocode[0] + ',' + geocode[1] + '/@' + geocode[0] + ',' + geocode[1] + ',' + geocode[2] + ',' + geocode[3])
            break

        except:

            sys.stdout.write(colored('\nwrong param\n', 'red'))
