# allBWM은 청백색을 갖는다. 용이다.
# adult는 날기 가능 child는 아직 안됨.
# BWM_001은 수컷이다. 19살이다. 불 속성.
# BWM_002는 암컷이다. 2살이다. 얼음 속성.

class allBWM:
    
    def __common__(self,fly,att,sex):
        self.color = "Blue&White"
        self.breed = "dragon"
        self.fly = fly
        self.att = att
        self.sex = sex
        
class adultBWM(allBWM):
    
    def __common__(self, att, sex):
        super().__common__(
            fly="Can",
            att=att,
            sex=sex,
        )
        self.adult = True
    
    def __adult__(self, age):
        print("I am {age} years-old, adult dragon")
        
class childBWM(allBWM):
    
    def __common__(self, att, se):
        super().__common__(
            "Can",
            att,
            se,
        )
        self.adult = False
    
    def __child__(self, age):
        print("grr..grr....({age} years-old)")
     
firstBWM = adultBWM(att="Fire",sex="Male",age=19)
# secondBWM = childBWM(
#             "Ice",
#             se="Female",
#             age=2)
    
        