from get_color_from_pair_number import *
from get_pair_number_from_color import *
from test_number_to_pair import *
from test_pair_to_number import *
from color_pair_to_string import *

def Reference_manual():
    refman_rows = []
    refman_columns = ["Pair_number","MajorColor" ,"MajorColor","MinorColor" ,"MinorColor"]
    refman_text = []
    refman_colors = []
    
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            Pair_number = get_pair_number_from_color(major_color,minor_color)
            refman_rows.append(Pair_number)
            refman_text.append([str(Pair_number), major_color,"",minor_color,""])
            refman_colors.append(["","",major_color,"",minor_color])
