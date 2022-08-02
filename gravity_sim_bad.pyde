sc_size = PVector(1000,700)
sph_list = []

class Sphere:
    
    def __init__(self,x,y):
        
        self.pos = PVector(x,y)
        self.vi = PVector(0,0)
        self.ma = 10
        self.rgb = [0,0,0]
        self.vfx = {
                    'r':30
                    }
        
    def exist(self):
        circle(self.pos.x,self.pos.y,self.vfx['r']*2)
        
    def move(self,targ):
        xRatio = (targ.pos.x-self.pos.x)/sqrt(pow(targ.pos.y-self.pos.y,2)+pow(targ.pos.x-self.pos.x,2))
        yRatio = (targ.pos.y-self.pos.y)/sqrt(pow(targ.pos.x-self.pos.x,2)+pow(targ.pos.y-self.pos.y,2))
        self.vi.x += xRatio*0.2
        self.vi.y += yRatio*0.2
        self.pos.x += self.vi.x
        self.pos.y += self.vi.y
        if self.pos.x + self.vfx['r'] >= sc_size.x or self.pos.x - self.vfx['r'] <= 0:
            self.vi.x *= -0.5
        if self.pos.y + self.vfx['r'] >= sc_size.y or self.pos.y - self.vfx['r'] <= 0:
            self.vi.y *= -0.5
        '''
        # fix the condition (use vector magnitudes instead of simply x or y components)
        if abs(self.pos.x+targ.pos.x) <= self.vfx['r']+targ.vfx['r']:
            svix = self.vi.x
            tvix = targ.vi.x
            self.vi.x = (self.ma-targ.ma)/(self.ma+targ.ma)*svix + 2*targ.ma/(self.ma+targ.ma)*tvix
            targ.vi.x = (targ.ma-self.ma)/(targ.ma+self.ma)*tvix + 2*self.ma/(targ.ma+self.ma)*svix
        
            sviy = self.vi.y
            tviy = targ.vi.y
            self.vi.y = (self.ma-targ.ma)/(self.ma+targ.ma)*sviy + 2*targ.ma/(self.ma+targ.ma)*tviy
            targ.vi.y = (targ.ma-self.ma)/(targ.ma+self.ma)*tviy + 2*self.ma/(targ.ma+self.ma)*sviy
        '''

def setup():
    size(int(sc_size.x),int(sc_size.y))
    background(255)
    
sph1 = Sphere(200,300)
sph2 = Sphere(500,400)
sph3 = Sphere(600,500)
sph_list.append(sph1)
sph_list.append(sph2)
sph_list.append(sph3)
def draw():
    background(255)
    for i in range(len(sph_list)):
        sph_list[i].exist()
        for j in range(len(sph_list)):
            if sph_list[j] != sph_list[i]:
                sph_list[i].move(sph_list[j])
    #sph1.pos.x,sph1.pos.y = mouseX,mouseY
    
