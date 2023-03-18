import csv
import requests
import pandas as pd
from datetime import datetime

now = datetime.now()
print("now =", now)
dt_string = now.strftime("_%d_%m_%Y_%H_")


def loadRSS(url, xml):

    resp = requests.get(url)

    # saving the xml file
    with open(xml , 'wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):
    df = pd.read_xml(xmlfile)
    return df




def main():
    # load rss from web to update existing xml file
    try:
        loadRSS('https://vrijeme.hr/hrvatska_n.xml', 'dhmz_data/'+dt_string+'hrv_abecedno.xml')
        vrijeme_hrv_abecedno = parseXML('hrv_abecedno.xml')
    except:
        print("No data to load!")
    try:
        loadRSS('https://vrijeme.hr/hrvatska1_n.xml', 'dhmz_data/'+dt_string+'hrv_regije.xml')
        vrijeme_hrv_regije = parseXML('hrv_regije.xml')
    except:
        print("No data to load!")
    try:
        loadRSS('https://vrijeme.hr/europa_n.xml', 'dhmz_data/'+dt_string+'europa.xml')
        vrijeme_eu = parseXML('europa.xml')
    except:
        print("No data to load!")
    try:
        loadRSS('https://vrijeme.hr/more_n.xml', 'dhmz_data/'+dt_string+'hrv_more.xml')
        hrv_more = parseXML('hrv_more.xml')
    except:
        print("No data to load!")
    try:
        loadRSS('https://vrijeme.hr/oborina.xml', 'dhmz_data/'+dt_string+'oborine.xml')
        oborine = parseXML('oborine.xml')
    except:
        print("No data to load!")
    try:
        loadRSS('https://vrijeme.hr/snijeg_n.xml', 'dhmz_data/'+dt_string+'snijeg.xml')
        snijeg = parseXML('snijeg.xml')
    except:
        print("No data to load!")
    try:
        loadRSS('https://vrijeme.hr/uvi.xml', 'dhmz_data/'+dt_string+'indexuv.xml')
        uv_index = parseXML('indexuv.xml')
    except:
        print("No data to load!")
    try:
        loadRSS('https://klima.hr/agro_bilten.xml', 'dhmz_data/'+dt_string+'dhmz_agro.xml')
        agro = parseXML('dhmz_agro.xml')
    except:
        print("No data to load!")
    try:
        loadRSS('https://vrijeme.hr/agro_temp.xml', 'dhmz_data/'+dt_string+'dhmz_agro_temp.xml')
        agro_temp = parseXML('dhmz_agro_temp.xml')
    except:
        print("No data to load!")

    try:
        loadRSS('https://klima.hr/agro7.xml', 'dhmz_data/'+dt_string+'proteklih_7dana.xml')
        proteklih_7dana = parseXML('proteklih_7dana.xml')
    except:
        print("No data to load!")

    my_df = parseXML("./dhmz_data/_02_03_2023_20_hrv_abecedno.xml")
    my_df.to_csv("./dhmz_data/_02_03_2023_20_hrv_abecedno.csv")

    my_df = parseXML("./dhmz_data/_02_03_2023_20_hrv_abecedno.xml")
    my_df.to_csv("./dhmz_data/_02_03_2023_20_hrv_abecedno.csv")

    my_df = parseXML("./dhmz_data/_02_03_2023_20_hrv_abecedno.xml")
    my_df.to_csv("./dhmz_data/_02_03_2023_20_hrv_abecedno.csv")

    my_df = parseXML("./dhmz_data/_02_03_2023_20_hrv_abecedno.xml")
    my_df.to_csv("./dhmz_data/_02_03_2023_20_hrv_abecedno.csv")




if __name__ == "__main__":
    main()
