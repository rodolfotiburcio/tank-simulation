import time

class Tank:
    def __init__(self):
        self.last_time = time.time()
        self.inflow = 10.0 #liters per sec
        self.outflow = 8.0 #liters per sec
        self.capacity = 100 #liters
        self.max_level = 0.9 # 90%
        self.low_level = 0.1 # 10%
        self.level = 0.0
        self.invalve = False
        self.outvalve = False

    def hi_level(self):
        return self.level >= self.max_level

    def lo_level(self):
        return self.level <= self.low_level

    def process(self):
        now = time.time()
        step_time = now - self.last_time
        self.last_time = now

        if self.invalve:
            self.level += step_time * self.inflow / self.capacity

        if self.outvalve:
            self.level -= step_time * self.outflow / self.capacity
        
        return {
            'lo_level':self.lo_level(),
            'hi_level':self.hi_level()
        }
        
