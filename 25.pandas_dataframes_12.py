import pandas as pd

staff_df = pd.DataFrame([
    {'Name' : 'Kelly', 'Role' : 'Director of HR'},
    {'Name' : 'Sally', 'Role' : 'Course liason'},
    {'Name' : 'James', 'Role' : 'grader'}
    ])
staff_df = staff_df.set_index('Name')

student_df = pd.DataFrame([
    {'Name' : 'James', 'School' : 'Business'},
    {'Name' : 'Mike', 'School' : 'Law'},
    {'Name' : 'Sally', 'School' : 'Engineering'}
    ])

student_df = student_df.set_index('Name')

print (staff_df)
print ()
print (student_df)

#Joins based on index
outer_joined_df = pd.merge(staff_df, student_df, how = 'outer', 
                           left_index = True, right_index = True)
print ()
print (outer_joined_df)

inner_joined_df = pd.merge(staff_df, student_df, how = 'inner', 
                           left_index = True, right_index = True)
print ()
print (inner_joined_df)

left_joined_df = pd.merge(staff_df, student_df, how = 'left', 
                          left_index = True, right_index = True)
print ()
print (left_joined_df)

right_joined_df = pd.merge(staff_df, student_df, how = 'right', 
                           left_index = True, right_index = True)
print ()
print (right_joined_df)

#Joins without index
student_df = student_df.reset_index()
staff_df = staff_df.reset_index()

left_join_df_2 = pd.merge(staff_df, student_df, how = 'left', 
                          left_index = False, right_index = False,
                          left_on = 'Name', right_on = 'Name')

print (left_join_df_2)

#Joins with conflicting columns present in both dataframes
staff_df['Location'] = ['State Street','Washinton Avenue','Washinton Avenue']
student_df['Location'] = ['1024 Billiard Avenue','Fraternity House #22','512 Wilson Cresent']

print("After Adding Location Column")
print(staff_df)
print(student_df)

joined_df_with_location_column_in_both = pd.merge(staff_df, student_df, how='left',
                                                left_on = 'Name',
                                                right_on = 'Name')
print("After joining with location column")
print(joined_df_with_location_column_in_both)
