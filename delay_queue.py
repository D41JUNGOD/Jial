class queue:
    up_name = ["의정부", "소요산", "동두천", "광운대", "청량리", "동묘앞", "양주", "창동"]
    down_name = ["인천", "구로", "서동탄", "신창", "천안", "병점"]
    uq,dq,delay_d,delay_u = [[0 for j in range(1000)] for i in range(10)],[[0 for j in range(1000)] for i in range(10)],[[0 for j in range(1000)] for i in range(10)],[[0 for j in range(1000)] for i in range(10)]
    uqct,dqct = [0]*10,[0]*10
    upct,downct = 0,0

    def find_n(self,st,ud):
        if ud == '상행':
            for i in range(len(self.up_name)):
                if st == self.up_name[i]:
                    return i
        else:
            for i in range(len(self.down_name)):
                if st == self.down_name[i]:
                    return i

    def make_queue(self):
        f = open("data/schedule_up.txt", "r",encoding='utf-8')
        ct = [0]*10
        while True:
            line = f.readline()
            if not line:
                break

            st,time = line.split(" ")
            i = self.find_n(st,'상행')
            self.delay_u[i][ct[i]] = -1
            self.uq[i][ct[i]] = time
            ct[i] += 1
        f.close()

        f = open("data/schedule_down.txt","r",encoding='utf-8')
        ct = [0] * 10
        while True:
            line = f.readline()
            if not line:
                break

            st,time = line.split(" ")
            i = self.find_n(st,'하행')
            self.delay_d[i][ct[i]] = -1
            self.dq[i][ct[i]] = time
            ct[i] += 1
        f.close()

    def pop_queue(self,st,ud,time):
        if ud == '상행':
            i = self.find_n(st,ud)
            t1 = self.uq[i][self.uqct[i]].split(":")
            t2 = time.split(":")

            sc_time = int(t1[0])*60 + int(t1[1])
            av_time = int(t2[0])*60 + int(t2[1])

            if sc_time > av_time:
                self.delay_u[i][self.uqct[i]] = -2
            else:
                self.delay_u[i][self.uqct[i]] = av_time - sc_time
            self.uqct[i] += 1

        else:
            i = self.find_n(st, ud)
            t1 = self.dq[i][self.dqct[i]].split(":")
            t2 = time.split(":")
            
            sc_time = int(t1[0]) * 60 + int(t1[1])
            av_time = int(t2[0]) * 60 + int(t2[1])
            
            if sc_time > av_time:
                self.delay_u[i][self.uqct[i]] = -2
            else:
                self.delay_d[i][self.dqct[i]] = av_time - sc_time
            self.dqct[i] += 1

    def update(self,st):
        if st == '상행':
            f = open("data/arrive_up.txt","r",encoding='utf-8')
            ct = 0
            while True:
                line = f.readline()
                if not line:
                    break
                ct += 1
                if ct > self.upct:
                    self.upct = ct
                    st,time = line.split(' ')
                    self.pop_queue(st,'상행',time)
        else:
            f = open("data/arrive_down.txt", "r",encoding='utf-8')
            ct = 0
            while True:
                line = f.readline()
                if not line:
                    break
                ct += 1
                if ct > self.downct:
                    self.downct = ct
                    st, time = line.split(' ')
                    self.pop_queue(st, '하행', time)
    
    def return_calc(self,i,j,k):
        if (k=="u"):
            return self.delay_u[i][j]
        elif (k=="d"):
            return self.delay_d[i][j]


def init(i,j,k):
    a = queue()
    a.make_queue()
    a.update('하행')
    a.update('상행')
    return a.return_calc(i,j,k)

if __name__ == "__main__":
    a = queue()
    a.make_queue()
    a.update('하행')
    print(a.delay_d)

