class person:
    def __init__(self,name,occ):
        self._Name=name             #Constructor
        self._Occ=occ


    def info(self):
        print(f"{self._Name} is {self._Occ} ")

    @property
    def name(self):
        print(self._Name)            #Getter
        # return self._Name

    @name.setter
    def name(self,new_name):         #Setter
        self._Name=new_name

    @property
    def occupation(self):            #Getter
        print(self._Occ)
    
    @occupation.setter
    def occupation(self,new_occ):    #Setter
        self._Occ=new_occ


a=person("Saurabh Gupta","traveller")
b=person("Nishant Gupta" ,"Businessman")
# print(a._Name)    this also accessable
a.name
a.name="Aksay"
a.occupation
a.occupation="Loco"

a.info()
b.info()
