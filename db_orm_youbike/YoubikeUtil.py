import json
import requests


def get_youbike_list():
    url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.gz'
    youbike = requests.get(url).text
    youbike = json.loads(youbike)

    youbike_list = []
    for i in range(1, 405):
        sno = ("%04d" % i)
        try:
            sno = youbike["retVal"][sno]['sno']
            sna = youbike["retVal"][sno]['sna']
            tot = int(youbike["retVal"][sno]['tot'])
            sbi = int(youbike["retVal"][sno]['sbi'])
            bemp = int(youbike["retVal"][sno]['bemp'])
            lat = float(youbike["retVal"][sno]['lat'])
            lng = float(youbike["retVal"][sno]['lng'])
            #print("%s %s %d %d %d %f %f" % (sno, sna, tot, sbi, bemp, lat, lng))
            dic = {}
            dic.setdefault('sno', sno)
            dic.setdefault('sna', sna)
            dic.setdefault('tot', tot)
            dic.setdefault('sbi', sbi)
            dic.setdefault('bemp', bemp)
            dic.setdefault('lat', lat)
            dic.setdefault('lng', lng)
            youbike_list.append(dic)
        except Exception as e:
            #print(e)
            None
    return youbike_list


def get_youbike_test():
    url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.gz'
    youbike = requests.get(url).text
    youbike = json.loads(youbike)

    for i in range(1, 405):
        sno = ("%04d" % i)
        try:
            sno = youbike["retVal"][sno]['sno']
            sna = youbike["retVal"][sno]['sna']
            tot = int(youbike["retVal"][sno]['tot'])
            sbi = int(youbike["retVal"][sno]['sbi'])
            bemp = int(youbike["retVal"][sno]['bemp'])
            lat = float(youbike["retVal"][sno]['lat'])
            lng = float(youbike["retVal"][sno]['lng'])
            print("%s %s %d %d %d %f %f" % (sno, sna, tot, sbi, bemp, lat, lng))
        except Exception as e:
            # print(e)
            None
