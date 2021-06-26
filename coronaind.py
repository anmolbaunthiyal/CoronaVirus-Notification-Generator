import requests
import json
from plyer import notification
import time


def notify_me(title, message):
    '''  Function for genrating notification using plyer module '''
    notification.notify(
        title=title,
        message=message,
        app_icon="covid.ico",
        timeout=10,
    )


if __name__ == '__main__':
    a = int(input("\t\t\tEnter notifiction interval in seconds:   "))
    b=int(input("\t\t\tEnter State for which you want to get status\n"
                "\t\t\t0 for whole India         1 for Maharastra         2 for Andhra Pradesh                 3 for Karnataka          4 for Tamil Nadu\n"
                "\t\t\t5 for Uttar Pradesh       6 for Delhi              7 for Kerala                         8 for West Bengal        9 for Odisha\n"
                "\t\t\t10 for Telangana         11 for Bihar             12 for Assam                         13 for Rajasthan         14 for Gujarat\n"
                "\t\t\t15 for Madhya Pradesh    16 for Chhattisgarh      17 for Haryana                       18 for Punjab            19 for Jharkhand\n"
                "\t\t\t20 for Jammu and Kashmir 21 for Uttarakhand       22 for Goa                           23 for Puducherry        24 for Tripura\n"
                "\t\t\t25 for Himachal Pradesh  26 for Manipur           27 for Chandigarh                    28 for Arunachal Pradesh 29 for Meghalaya\n"
                "\t\t\t30 for Nagaland          31 for Ladakh            32 for Andaman and Nicobar Islands   33 for Sikkim            34 for Dadra and Nagar Haveli and Daman and Diu\n"
                "\t\t\t35 for Mizoram           37 for Lakshadweep\n"
                "\t\t\tEnter your Choice :  "))
    data={0:'India',1:'Maharastra',2:'Andhra Pradesh',3:'Karnataka',4:'Tamil Nadu',5:'Uttar Pradesh',6:'Delhi',7:'Kerala',8:'West Bengal',9:'Odisha',10:'Telangana',
          11:'Bihar',12:'Assam',13:'Rajasthan',14:'Gujarat',15:'Madhya Pradesh',16:'Chhattisgarh',17:'Haryana',18:'Punjab',19:'Jharkhand',20:'Jammu and Kashmir',
          21:'Uttarakhand',22:'Goa',23:'Puducherry',24:'Tripura',25:'Himachal Pradesh',26:'Manipur',27:'Chandigarh',28:'Arunachal Pradesh',29:'Meghalaya',30:'Nagaland',
          31:'Ladakh',32:'Andaman and Nicobar Islands',33:'Sikkim',34:'Dadra and Nagar Haveli and Daman and Diu',35:'Mizoram',37:'Lakshadweep'}
    r = requests.get('https://api.covid19india.org/data.json')
    data_json = r.json()
    confirmed_str = json.dumps(data_json['statewise'][b]['confirmed'])
    active_str = json.dumps(data_json['statewise'][b]['active'])
    cured_recovered = json.dumps(data_json['statewise'][b]['recovered'])
    deaths = json.dumps(data_json['statewise'][b]['deaths'])
    while True:
            notify_title = f"Covid-19 {data[b]} Status"
            notify_text = f"Confirmed : {confirmed_str}\nActive Cases : {active_str}\nCured/Discharged : {cured_recovered}\nDeaths : {deaths}"
            notify_me(notify_title,notify_text)
            time.sleep(a)