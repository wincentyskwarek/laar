    """
        if speed>0:
            self.wheel15p.ChangeDutyCycle(speed15)
            self.wheel3p.ChangeDutyCycle(speed3)
            self.wheel26p.ChangeDutyCycle(speed26)
            self.wheel4p.ChangeDutyCycle(speed4)
            self.wheel15t.ChangeDutyCycle(0)
            self.wheel3t.ChangeDutyCycle(0)
            self.wheel26t.ChangeDutyCycle(0)
            self.wheel4t.ChangeDutyCycle(0)                       
        else:
            speed15=-speed15
            speed26=-speed26
            speed3=-speed3
            speed4=-speed4
            self.wheel15t.ChangeDutyCycle(speed15)
            self.wheel3t.ChangeDutyCycle(speed3)
            self.wheel26t.ChangeDutyCycle(speed26)
            self.wheel4t.ChangeDutyCycle(speed4)
            self.wheel15p.ChangeDutyCycle(0)
            self.wheel3p.ChangeDutyCycle(0)
            self.wheel26p.ChangeDutyCycle(0)
            self.wheel4p.ChangeDutyCycle(0)

                

        angle=(angle)/(14.29)

        
        

        self.servo1.ChangeDutyCycle(7.5+alpha1)
        self.servo2.ChangeDutyCycle(7.2+alpha2)
        
        self.servo5.ChangeDutyCycle(7.2-alpha1)
        self.servo6.ChangeDutyCycle(7-alpha2)"""