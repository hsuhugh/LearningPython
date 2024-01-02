#型別轉換

#name = 'john'
#age = 30
#gpa = 2.5
#student = False

#print(type(name))
#print(type(age))
#print(type(gpa))
#print(type(student))

#age = float(age)
#print(age)
#print(type(age))

x = 10
y = 2.0
z=x/y
print(z)
print(type(z))

#顯示型別轉換的補充說明：
#顯示型別轉換的方法有一些input的限制,例如如果要使用int()方法,input就不會接受像string這種的資料型態,
#但如果是布林的資料型態的話,int()方法是可以接受的,最後output的結果會為0 (input 為 False 時）或1 (input 為 True 時）