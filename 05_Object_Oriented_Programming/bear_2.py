import datetime
class Bear:
    logfile_name = 'bear_log'
    bear_num     = 0
    bear_names   = []
    def __init__(self, name):
        self.name = name
        print('Made a bear called %s' %(name))
        self.logfile = open(Bear.logfile_name, 'a')
        Bear.bear_num += 1
        self.created = datetime.datetime.now()
        self.my_num = Bear.bear_num
        self.logfile.write('[%s] created bear #%i named %s\n' %
                          (datetime.datetime.now(), Bear.bear_num, self.name))
        self.logfile.flush()
        
    def growl(self, nbeep = 5):
        print('\a'*nbeep)
        
    def __del__(self):
        print('Bang! %s is no longer' % self.name)
        self.logfile.write('[%s] deleted bear #%i named %s\n' % \
                          (datetime.datetime.now(), self.my_num, self.name))
        self.logfile.flush()
        #Decrease the number of bears in the population
        Bear.bear_num -= 1
        self.logfile.close()
        
    def __str__(self):
        age = datetime.datetime.now() - self.created
        return 'Name = %s bear (age %i) number = %i (population %i)' % \
                (self.name, age, self.my_num, Bear.bear_num)