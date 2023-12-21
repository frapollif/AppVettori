#%%
import re
import numpy as np
user_input="A(20,30,34) \n B(12,11,10) \n C(45,34,30)"

points_pattern="[A-Z]\(.+\)"
points_name_pattern="([A-Z])"
points_coord_pattern="\(([-]?\d+),([-]?\d+),([-]?\d+)\)"
points_string=re.findall(pattern=points_pattern,string=user_input, flags=re.MULTILINE)


points_dict={}
for str_point in points_string:
    print(str_point)
    point_name=re.findall(pattern=points_name_pattern,string=str_point)
    point_coord=re.findall(pattern=points_coord_pattern,string=str_point)
    coord_array=np.array([int(point_coord[0][0]),int(point_coord[0][1]),int(point_coord[0][2])])
    points_dict[point_name[0]]=coord_array
print(points_dict)


# %%
