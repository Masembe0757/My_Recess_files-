#EXERCISE ONE
#1
female_names = ["Gina","Anna","Doroth","Elizabeth","Edith"]
#2
female_names[0] = "Annet"
print(female_names)
#3
female_names.append("Lucy")
print(female_names)
#4
female_names.insert(2,"Bathel")
print(female_names)
#5
female_names.pop(3)
print(female_names)
#6
print(female_names[-1])
#7
numbers = ["A","B","C","D","E","F","G"] 
print(numbers[2:5])
#8
countries = ["Uganda","Tanzania","Burundi"]
countries1 = countries.copy()
print(countries1)
#9
count = 1
for x in countries :
    print("Country ",count, " is ",x)
    count +=1
    
#10
animals =["cow","goat","horse","sheep","kaote"]
animals.sort(reverse=True)
print(animals)

#11
print("The following animal names have letter a in them")
for x in animals :
    if "a" in x :
        
        print(x)
#12
f_name =["Sendi"]
l_name = ["Joseph"]
full_name = f_name+l_name
print(full_name)

#EXERCISE TWO
#1
x = ("samsung","iphone","tecno","redmi")
print("My favorite phone is an ",x[1])

#2
print("The second last phone is ",x[-2])

#3
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print(x)

#4
y_list = list(x)
y_list.append("Huawei")
x = tuple(y_list)
print(x)

#5
counter = 1
for member in x :
    print("Phone ", counter ," is ",member)
    counter+=1 
#6
b_list = list(x)
b_list.pop(0)
x= tuple(b_list)
print(x)

#7
cities = tuple({"Kampala","Mbarara","Gulu","Fortportal"})
print(cities)

#8 unpack
for ct in cities:
    print(ct) 

#9
print(cities[1:4])
#10
f_name = tuple({"Sendi"})
l_name = tuple({"Joseph"})
f_name+=l_name
print(f_name)
#11
colors = ("red","blue")
print(colors*3)
#12
thistuple = (1,3,7,8,7,5,4,6,8,5)
num = 0
for x in thistuple :
    if x is 8 :
        num+=1
print("The number 8 appears ",num," times")

#EXERCISE 3

#1
beverages = set({"fanta","mirinda","juice"})
#2
beverages.add("cola")
beverages.add("sprite")
print(beverages)
#3
myset = {"oven","kettle","microwave","refrigerator"}
if "microwave" in myset:
    print("microwave is present")
else:
    print("not present")
    
#4
myset.remove("kettle")
print(myset)

#5
for my in myset :
    print(my)

#6
numbers_1 = {1,2,3,4}
numbers_2 =[5,6]
combined =numbers_1.union(set(numbers_2))
print(combined)
#7
names ={"Sendi","Joseph"}
age ={19}
print(names.union(age))

#EXERCISE 4
#1
status ="online"
users = 34
print("There are ",34," "+status+" users")
#2
txt = "    Helo,  Uganda"
print(txt.replace(" ",""))

#3
txt.upper()
#4
kxt = txt.replace(" ","").replace('U','V')
print(kxt)
#5
y = "I am proudly Ugandan"
print(y[1:4])
#6
# x = "All"Data Scientists" are cool!" error code
x = "All \"Data Scientists\" are cool!"
print(x)

#EXERCISE FIVE
#1
Shoes = {"brand":"Nick","color":"black","size":40}
print(Shoes["size"])

#2
Shoes["brand"] ="adidas"
#3
Shoes.update({"type":"sneakers"})
#4
for x in Shoes:
    print(x)
#5
for y in Shoes:
    print(Shoes[y])
#6
if "size" in Shoes.keys():
    print("Key exists")
else:
    print("Doesnt exist")
#7
for key in Shoes:
    print(key," is ",Shoes[key])
#8
Shoes.pop("color")
#9
Shoes.clear()
#10
spouses = {"David":"Anna","John":"Matha","Joseph":"Mary"}
spouses_b = spouses.copy()
print(spouses_b)
#11
occupation_price ={"lecturer":5000000,"Engineer":5600000}
chores_time ={"mopping":"6 am","cooking": "12 pm"}
People = {"male":occupation_price,"female":chores_time}
print("Females cook at ",People["female"]["cooking"])
print("Lectures are paid ",People["male"]["lecturer"],"shillings")


    

