from flask import *
from delay_queue import *
import random

app = Flask(__name__)
uct,dct = [0]*10,[0]*10
#app.debug = True
@app.route('/')
def index():
    return render_template("index.html")

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
    try:
        get_val = request.args.get('info')
        st,time = get_val.replace("%20"," ").split()
    
        delay_time = random.randint(1,5)
        resault = st + "행 " + str(delay_time) +" 분 지연입니다."
    except:
        resault = ""
    return render_template("main.html", left=left,right=right,k=254, info=resault)

if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0', port=8888)

