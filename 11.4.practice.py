#11.4.모듈 직접 실행
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
trip_to = thiland.ThilandPackage()
trip_to.detail()

