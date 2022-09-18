#11.5.패키지, 모듈위치
#import travel.thiland
#import travel.thiland.ThilandPackage
#trip_to = travel.thiland.ThilandPackage()
#trip_to.detail()

#from travel.thiland import ThilandPackage
#trip_to = ThilandPackage()
#trip_to.detail()

#from travel import vietnam
#trip_to = vietnam.VietnamPackage()
#trip_to.detail() 

#from random import *
from travel import *
#trip_to = vietnam.VietnamPackage()
#trip_to = thiland.ThilandPackage()
#trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thiland))
