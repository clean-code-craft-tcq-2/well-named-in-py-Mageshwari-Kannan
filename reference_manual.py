from get_color_from_pair_number import *
from get_pair_number_from_color import *
from test_number_to_pair import *
from test_pair_to_number import *
from color_pair_to_string import *
from color_pair_to_string import MAJOR_COLORS
from color_pair_to_string import MINOR_COLORS

def reference_manual():
    
    for i, major in enumerate(MAJOR_COLORS):
        for j, minor in enumerate(MINOR_COLORS):
            print(f'{i * 5 + j} | {major} | {minor}')
