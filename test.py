#%%
import re
user_input="A(20,30,34) \n B(12,11,10) \n C(45,34,30)"

points_pattern="[A-Z]\(.+\)"
points_name_pattern="([A-Z])"
points_coord_pattern="\(([-]?\d+,[-]?\d+,[-]?\d+)\)"
points_string=re.findall(pattern=points_pattern,string=user_input, flags=re.MULTILINE)

for str_point in points_string:
       
    point_name=re.match(pattern=points_name_pattern,string=str_point).group(1)
    point_coord=re.match(pattern=points_coord_pattern,string=str_point).group(1)
    
    print(point_name)


# %%
