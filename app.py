# stations
import subprocess
from ok import OK_STATION
from q8 import Q8_STATION
from f24 import F24_STATION
from circle import CIRCLE_STATION
from ingo import INGO_STATION
from goon import GOON_STATION

# load prices
print(OK_STATION().get_prices())
print(Q8_STATION().get_prices())
print(F24_STATION().get_prices())
print(CIRCLE_STATION().get_prices())
print(INGO_STATION().get_prices())
print(GOON_STATION().get_prices())