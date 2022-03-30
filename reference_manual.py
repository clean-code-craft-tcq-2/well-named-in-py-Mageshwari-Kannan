from get_color_from_pair_number import *
from get_pair_number_from_color import *
from test_number_to_pair import *
from test_pair_to_number import *
from color_pair_to_string import *
from color_pair_to_string import MAJOR_COLORS
from color_pair_to_string import MINOR_COLORS
import matplotlib.pyplot as plt

def reference_manual():
    color_pair_rows = []
    color_pair_text = []
    color_pair_colors = []
    color_pair_columns = ["ColorCode","MajorColor_Name","MajorColor","MinorColor_Name","MinorColor"]

    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            colorcode = get_pair_number_from_color(major_color,minor_color)
            print("ColorCode: ",colorcode,"- MajorColor: "+major_color," ; MinorColor: "+minor_color)
            color_pair_rows.append(colorcode)
            color_pair_text.append([str(colorcode), major_color,"",minor_color,""])
            if(minor_color =="Slate"): minor_color = "slategrey"
            color_pair_colors.append(['White',"White",major_color,"White",minor_color])

    colorPair, colorPair_Axes = plt.subplots(figsize = (6,8),)

    colorPair_Axes.xaxis.set_visible(False) 
    colorPair_Axes.yaxis.set_visible(False)

    colorPair_Axes.table(cellText=color_pair_text, rowLabels=color_pair_rows, colLabels=color_pair_columns, cellColours=color_pair_colors, loc='top', bbox=[0,0,1,1])
    plt.savefig("Color_Pair_reference_manual.pdf",bbox_inches='tight')
    plt.show()
