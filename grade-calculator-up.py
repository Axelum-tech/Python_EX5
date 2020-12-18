grade_1=9.0
grade_2=7.0
grade_3=2.5


grade_avg   =(grade_1+grade_2+grade_3)/3
grade_avg   =round(grade_avg, 2 )

good_result=grade_avg > 7.0

print("Average grade", grade_avg)
print("is it a good grade?", good_result)
