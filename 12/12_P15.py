import math
class Circle:
    def __init__(self,index,x,y,r):
        self.index = index
        self.x = x
        self.y = y
        self.r = r
    def line_intersection(self,line):
        # หาจุดตัดของ “เส้นตรง” และวงกลม ค่าที่ return เป็น tuple ของจานวนจุดตัด ตามด้วยพิกัดของจุดตัดที่เป็นคาตอบ
        if line.x1 != line.x2:
            # line: y = Mx+B
            M = (line.y2-line.y1)/(line.x2-line.x1)
            B = line.y1-M*line.x1
            # แก้สมการจาก (x-self.x)**2+(y-self.y)**2 = self.r**2
            a = M**2+1
            b = -2*self.x + 2*M*(B-self.y)
            c = self.x**2+(B-self.y)**2-self.r**2
            if b**2 > 4*a*c:
                ans1 = (-b + math.sqrt(b**2-4*a*c))/2/a
                ans2 = (-b - math.sqrt(b**2-4*a*c))/2/a
                return (2,(ans1,M*ans1+B),(ans2,M*ans2+B))
            elif b**2 == 4*a*c:
                return (1,(-b/2/a,M*(-b/2/a)+B))
            else:
                return (0,)
        else:
            if self.r**2 == (line.x1-self.x)**2:
                return (1,(line.x1,self.y))
            elif self.r**2 > (line.x1-self.x)**2:
                rr = math.sqrt(self.r**2 - (line.x1-self.x)**2)
                ans1 = rr+self.y
                ans2 = rr-self.y
                return (2,(line.x1,ans1),(line.x2,ans2))
            else:
                return (0,)
    def contain_point(self,px,py):
        # ทดสอบว่าจุดอยู่ในวงกลมหรือไม่ ถ้าอยู่จะคืน True ถ้าไม่อยู่ จะคืน False
        if distance(self.x,self.y,px,py) <= self.r:
            return True
        return False
    def line_in_circle(self,line):
        # คืน True ถ้า “ส่วนของเส้นตรง” ตัด ซ้อนทับ หรือสัมผัสวงกลม นอกจากนั้นให้คืน False
        if self.contain_point(line.x1, line.y1) or self.contain_point(line.x2, line.y2): # ถ้าจุดปลายของ “ส่วนของเส้นตรง” ซักข้างอยู่ในวงกลม ให้คืนค่า True
            return True
        ret = self.line_intersection(line) # หาคา ตอบว่า “เส้นตรง” ตัดกับวงกลมกี่จุด
        if ret[0] == 0: # ผลเฉลยของสมการบอกว่า ไม่มีจุดตัดของวงกลมกับ “เส้นตรง” แสดงว่าไม่มีจุดตัดกับ “ส่วนของเส้นตรง” ด้วย
            return False
        if ret[0] == 1: # ผลเฉลยของสมการบอกว่า “เส้นตรง” สัมผัสวงกลม 1 จุด
        # ให้เช็คด้วยว่าจุดนั้นอยู่ใน “ส่วนของเส้นตรง” หรือไม่ ถ้าอยู่ให้คืนค่า True ถ้าไม่อยู่ให้คืนค่า False
            return line.contain_point(*ret[1])
        if ret[0] == 2: # ผลเฉลยของสมการบอกว่า “เส้นตรง” ตัดวงกลม 2 จุด
        # ให้เช็คด้วยว่าใน 2 จุดนั้น มีซักจุดอยู่ใน “ส่วนของเส้นตรง” หรือไม่ ถ้าอยู่ให้คืนค่า True ถ้าไม่อยู่ให้คืนค่า False
            return line.contain_point(*ret[1]) or line.contain_point(*ret[2])
def distance(x1,y1,x2,y2):
    # หาระยะห่างระหว่างจุดสองจุด
    return ((x1-x2)**2+(y1-y2)**2)**0.5
class Line:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def contain_point(self,px,py):
        # คืน True ถ้าจุดอยู่บน “ส่วนของเส้นตรง” คืน False ถ้าจุดไม่อยู่บน “ส่วนของเส้นตรง”
        if not (min(self.y1,self.y2) <= py <= max(self.y1,self.y2)):
            return False
        if self.x1 == self.x2:
            return px == self.x1
        else:
            return abs((self.y1-py)*(self.x2-self.x1)-(self.y2-self.y1)*(self.x1-px))<1e-5

# ส่วนของโปรแกรมหลัก
n = int(input().strip())
line_input = [int(e) for e in input().strip().split()]
line = Line(*line_input)

output = []

for i in range(n):
    circle_input = [int(e) for e in input().strip().split()]
    circle = Circle(*circle_input)
    if circle.line_in_circle(line): # ”ส่วนของเส้นตรง” ตัดหรือสัมผัสวงกลม
        output.append(circle.index) # เติมหมายเลขวงกลมลงใน output

if len(output) == 0:
    print('Not Found')
else:
    print(' '.join([str(e) for e in output]))