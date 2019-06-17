import requests
import xml.etree.ElementTree as ET
from time import sleep
from datetime import datetime

def exception(fir, sec):
    s_time = fir[:-1].split(" ")[1]
    e_time = sec[:-1].split(" ")[1]

    if s_time.split(":")[0] == "24":
        s_time = s_time.split(":")[0].replace("24", "00") + ":" + s_time.split(":")[1] + ":" + s_time.split(":")[2]
    if e_time.split(":")[0] == "24":
        e_time = e_time.split(":")[0].replace("24", "00") + ":" + e_time.split(":")[1] + ":" + e_time.split(":")[2]

    s_time = datetime.strptime(s_time, "%H:%M:%S")
    e_time = datetime.strptime(e_time, "%H:%M:%S")
    if e_time < s_time:
        tmp = e_time
        e_time = s_time
        s_time = tmp

    offset = ((e_time - s_time) + datetime.min).time()
    final = datetime(1900, 1, 1, 0, 2, 00).time()

    return final > offset

def parse_up():
    arrive_final = None

    while True:
        try:

            url = "http://swopenapi.seoul.go.kr/api/subway/sample/xml/realtimeStationArrival/1/1/%EB%82%A8%EC%98%81"
            r = requests.get(url)

        except:
            #print("HTTP Requests Error")
            continue

        if r.status_code != 503:
            data = []
            xml = ET.fromstring(r.text)

            for parent in xml.getiterator():
                for child in parent:
                    data.append(child.text)

            if len(data) < 10:
                #print("Data Lack")
                continue

            statn_arrive = data[18] + " 도착"
            if statn_arrive == data[-3]:                        #if arrive
                bstatn = data[-5]
                arvtime = data[-4].split(" ")[1].split(".")[0]
                arrive_var = bstatn + " " + arvtime + "\n"

                if ' (급행)' in arrive_var:
                    arrive_var = arrive_var.replace(" (급행)","")

                if ' (막차)' in arrive_var:
                    arrive_var = arrive_var.replace(" (막차)", "")

                if ' (첫차)' in arrive_var:
                    arrive_var = arrive_var.replace(" (첫차)", "")

                if arrive_var != arrive_final:
                    if arrive_final != None and arrive_var.split(" ")[0] == arrive_final.split(" ")[0]:     #Exception
                        if exception(arrive_final,arrive_var):
                            arrive_final = arrive_var
                            continue

                    f = open("data/arrive_up.txt","a",encoding='utf-8')
                    f.writelines(arrive_var)
                    #print("Data Write Success")
                    f.close()
                    arrive_final = arrive_var

            else:
                continue

        else:
            #print("503 Server error")
            pass
        
        sleep(3)

def parse_down_3():
    url = "http://swopenapi.seoul.go.kr/api/subway/sample/xml/realtimeStationArrival/3/3/%EB%82%A8%EC%98%81"
    arrive_final = None

    while True:
        try:
            r = requests.get(url)
        except:
            #print("HTTP Requests Error")
            continue
        try:
            if r.status_code != 503:
                data = []
                xml = ET.fromstring(r.text)

                for parent in xml.getiterator():
                    for child in parent:
                        data.append(child.text)

                if len(data) < 10:
                    #print("Data Lack")
                    continue

                if data[12] != '하행':
                    continue

                statn_arrive = data[18] + " 도착"

                if statn_arrive == data[-3]:  # if arrive
                    bstatn = data[-5]
                    arvtime = data[-4].split(" ")[1].split(".")[0]
                    arrive_var = bstatn + " " + arvtime + "\n"

                    if ' (급행)' in arrive_var:
                        arrive_var = arrive_var.replace(" (급행)", "")

                    if ' (막차)' in arrive_var:
                        arrive_var = arrive_var.replace(" (막차)", "")

                    if ' (첫차)' in arrive_var:
                        arrive_var = arrive_var.replace(" (첫차)", "")

                    if arrive_var != arrive_final:
                        if arrive_final != None and bstatn == arrive_final.split(" ")[0]:  # Exception
                            if exception(arrive_final, arrive_var):
                                arrive_final = arrive_var
                                continue

                        f = open("data/arrive_down.txt", "a",encoding='utf-8')
                        f.writelines(arrive_var)
                        #print("Data Write Success")
                        f.close()
                        arrive_final = arrive_var

                else:
                    continue

            else:
                #print("503 Server error")
                pass

            sleep(1)

        except Exception as err:
            print(err)


def parse_down_4():
    url = "http://swopenapi.seoul.go.kr/api/subway/sample/xml/realtimeStationArrival/4/4/%EB%82%A8%EC%98%81"

    arrive_final = None

    while True:
        try:
            r = requests.get(url)
        except:
            # print("HTTP Requests Error")
            continue
        try:
            if r.status_code != 503:
                data = []
                xml = ET.fromstring(r.text)

                for parent in xml.getiterator():
                    for child in parent:
                        data.append(child.text)

                if len(data) < 10:
                    # print("Data Lack")
                    continue

                if data[12] != '하행':
                    continue

                statn_arrive = data[18] + " 도착"
                if statn_arrive == data[-3]:  # if arrive
                    bstatn = data[-5]
                    arvtime = data[-4].split(" ")[1].split(".")[0]
                    arrive_var = bstatn + " " + arvtime + "\n"

                    if ' (급행)' in arrive_var:
                        arrive_var = arrive_var.replace(" (급행)", "")

                    if ' (막차)' in arrive_var:
                        arrive_var = arrive_var.replace(" (막차)", "")

                    if ' (첫차)' in arrive_var:
                        arrive_var = arrive_var.replace(" (첫차)", "")

                    if arrive_var != arrive_final:
                        if arrive_final != None and bstatn == arrive_final.split(" ")[0]:  # Exception
                            if exception(arrive_final, arrive_var):
                                arrive_final = arrive_var
                                continue

                        f = open("data/arrive_down.txt", "a", encoding='utf-8')
                        f.writelines(arrive_var)
                        # print("Data Write Success")
                        f.close()
                        arrive_final = arrive_var

                else:
                    continue

            else:
                # print("503 Server error")
                pass

            sleep(1)

        except Exception as err:
            print(err)

def parse_down_2():
    url = "http://swopenapi.seoul.go.kr/api/subway/sample/xml/realtimeStationArrival/2/2/%EB%82%A8%EC%98%81"

    arrive_final = None

    while True:
        try:
            r = requests.get(url)
        except:
            #print("HTTP Requests Error")
            continue
        try:
            if r.status_code != 503:
                data = []
                xml = ET.fromstring(r.text)

                for parent in xml.getiterator():
                    for child in parent:
                        data.append(child.text)

                if len(data) < 10:
                    #print("Data Lack")
                    continue

                if data[12] != '하행':
                    continue

                statn_arrive = data[18] + " 도착"

                if statn_arrive == data[-3]:  # if arrive
                    bstatn = data[-5]
                    arvtime = data[-4].split(" ")[1].split(".")[0]
                    arrive_var = bstatn + " " + arvtime + "\n"

                    if ' (급행)' in arrive_var:
                        arrive_var = arrive_var.replace(" (급행)", "")

                    if ' (막차)' in arrive_var:
                        arrive_var = arrive_var.replace(" (막차)", "")

                    if ' (첫차)' in arrive_var:
                        arrive_var = arrive_var.replace(" (첫차)", "")

                    if arrive_var != arrive_final:
                        if arrive_final != None and bstatn == arrive_final.split(" ")[0]:  # Exception
                            if exception(arrive_final, arrive_var):
                                arrive_final = arrive_var
                                continue

                        f = open("data/arrive_down.txt", "a",encoding='utf-8')
                        f.writelines(arrive_var)
                        #print("Data Write Success")
                        f.close()
                        arrive_final = arrive_var

                else:
                    continue

            else:
                #print("503 Server error")
                pass

            sleep(1)

        except Exception as err:
            print(err)

def parse_down_5():
    url = "http://swopenapi.seoul.go.kr/api/subway/sample/xml/realtimeStationArrival/5/5/%EB%82%A8%EC%98%81"

    arrive_final = None

    while True:
        try:
            r = requests.get(url)
        except:
            #print("HTTP Requests Error")
            continue
        try:
            if r.status_code != 503:
                data = []
                xml = ET.fromstring(r.text)

                for parent in xml.getiterator():
                    for child in parent:
                        data.append(child.text)

                if len(data) < 10:
                    #print("Data Lack")
                    continue

                if data[12] != '하행':
                    continue

                statn_arrive = data[18] + " 도착"

                if statn_arrive == data[-3]:  # if arrive
                    bstatn = data[-5]
                    arvtime = data[-4].split(" ")[1].split(".")[0]
                    arrive_var = bstatn + " " + arvtime + "\n"

                    if ' (급행)' in arrive_var:
                        arrive_var = arrive_var.replace(" (급행)", "")

                    if ' (막차)' in arrive_var:
                        arrive_var = arrive_var.replace(" (막차)", "")

                    if ' (첫차)' in arrive_var:
                        arrive_var = arrive_var.replace(" (첫차)", "")

                    if arrive_var != arrive_final:
                        if arrive_final != None and bstatn == arrive_final.split(" ")[0]:  # Exception
                            if exception(arrive_final, arrive_var):
                                arrive_final = arrive_var
                                continue

                        f = open("data/arrive_down.txt", "a",encoding='utf-8')
                        f.writelines(arrive_var)
                        #print("Data Write Success")
                        f.close()
                        arrive_final = arrive_var

                else:
                    continue

            else:
                #print("503 Server error")
                pass

            sleep(1)

        except Exception as err:
            print(err)

def parse_down_6():
    url = "http://swopenapi.seoul.go.kr/api/subway/sample/xml/realtimeStationArrival/6/6/%EB%82%A8%EC%98%81"

    arrive_final = None

    while True:
        try:
            r = requests.get(url)
        except:
            #print("HTTP Requests Error")
            continue
        try:
            if r.status_code != 503:
                data = []
                xml = ET.fromstring(r.text)

                for parent in xml.getiterator():
                    for child in parent:
                        data.append(child.text)

                if len(data) < 10:
                    #print("Data Lack")
                    continue

                if data[12] != '하행':
                    continue

                statn_arrive = data[18] + " 도착"

                if statn_arrive == data[-3]:  # if arrive
                    bstatn = data[-5]
                    arvtime = data[-4].split(" ")[1].split(".")[0]
                    arrive_var = bstatn + " " + arvtime + "\n"

                    if ' (급행)' in arrive_var:
                        arrive_var = arrive_var.replace(" (급행)", "")

                    if ' (막차)' in arrive_var:
                        arrive_var = arrive_var.replace(" (막차)", "")

                    if ' (첫차)' in arrive_var:
                        arrive_var = arrive_var.replace(" (첫차)", "")

                    if arrive_var != arrive_final:
                        if arrive_final != None and bstatn == arrive_final.split(" ")[0]:  # Exception
                            if exception(arrive_final, arrive_var):
                                arrive_final = arrive_var
                                continue

                        f = open("data/arrive_down.txt", "a",encoding='utf-8')
                        f.writelines(arrive_var)
                        #print("Data Write Success")
                        f.close()
                        arrive_final = arrive_var

                else:
                    continue

            else:
                #print("503 Server error")
                pass

            sleep(1)

        except Exception as err:
            print(err)

if __name__ == '__main__':
    parse_down_2()
