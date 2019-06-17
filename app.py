from flask import *
from delay_queue import *
import random
import datetime

app = Flask(__name__)
uct,dct = [0]*10,[0]*10
#app.debug = True
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/door')
def door():
    dt = datetime.datetime.now()
    hour = str(dt.hour)
    print(hour)
    info = ""
    time = "5:17:00"
    if hour=="5":
        time="5:17:00"
    if hour=="6":
        time="6:04:00"
    if hour=="7":
        time="7:01:00"
    if hour=="8":
        time="8:01:00"
    if hour=="9":
        time="9:02:00"
    if hour=="10":
        time="10:00:00"
    if hour=="11":
        time="11:03:00"
    if hour=="12":
        time="12:02:00"
    if hour=="13":
        time="13:03:00"
    if hour=="14":
        time="14:02:00"
    if hour=="15":
        time="15:03:00"
    if hour=="16":
        time="16:03:00"
    if hour=="17":
        time="17:03:00"
    if hour=="18":
        time="18:00:00"
    if hour=="19":
        time="19:03:00"
    if hour=="20":
        time="20:01:00"
    if hour=="21":
        time="21:00:00"
    if hour=="22":
        time="22:04:00"
    if hour=="23":
        time="23:03:00"
    if hour=="24":
        time="24:12:00"
    try:
        get_val = request.args.get('info')
        return """<script>location.href="/main?info="""+get_val+"""#"""+time+"""\"</script>"""
    except:
        get_val ="none"
        return """<script>location.href=\"/main#"""+time+"""\"</script>"""

@app.route('/main', methods = ['GET', 'POST'])
def main():
    f = open("./data/schedule_up.txt", "r", encoding="utf-8")
    f2 = open("./data/schedule_down.txt", "r", encoding="utf-8")
    f3 = open("./data/up_arr.txt", "r", encoding="utf-8")
    f4 = open("./data/down_arr.txt","r",encoding="utf-8")
    left= f.readlines()
    right = f2.readlines()
    up_arr = f3.readlines()
    down_arr = f4.readlines()
    index = int()
    try:
        get_val = request.args.get('info')
        st,time = get_val.replace("%20"," ").split()
         
        if st in a.up_name:
            #print("up")
            k = "u"
            a.update("상행")
            for j, l in enumerate(left):
                if get_val.replace(" ","").replace("\n","") == l.replace(" ","").replace("\n","") :
                    #print(j,get_val, l)
                    index = j
            f3_line = up_arr[index].replace("up_ji[","").replace("][", ",").replace("]","")
            _i, _j = f3_line.split(",")
        
        elif st in a.down_name:
            #print("down")
            k = "d"
            a.update("하행")
            for j, l in enumerate(right):
                if get_val.replace(" ","").replace("\n","") == l.replace(" ","").replace("\n",""): 
                    #print(j,get_val,l)
                    index = j
            f3_line = down_arr[index].replace("down_ji[","").replace("][",",").replace("]","")
            _i, _j = f3_line.split(",") 

            #print(f3_line)
        
        
        delay_time = a.return_calc(int(_i),int(_j),k)
        if delay_time == -1:
            resault = "열차가 아직 도착하지않았습니다."
        elif delay_time == 0 or delay_time == -2:
            resault = "지연이 아닙니다."
        else:
            resault = st + "행 " + str(delay_time) +"분 지연입니다."
    except:
        resault=""

    return render_template("main.html", left=left,right=right,k=254, info=resault)
    
    

if __name__ == '__main__':
    global a 
    a = queue()
    a.make_queue()
    app.debug = True
    app.run(host='0.0.0.0', port=8888)

