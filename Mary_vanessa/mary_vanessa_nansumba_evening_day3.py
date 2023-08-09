# Create a list with 5 items (names of people) and write a python program to output the 2nd item.
#Write a python program to loop through the list of countries
#lists
#1
fruits = ["apple", "banana", "cherry","orange", "berry", ]
print (fruits[1])
#2
print(fruits)
fruits[0] = "jackfruit"
print(fruits)
#3
#add a new item 
fruits.append("grapes")
print(fruits)
#4
fruits[2]="Bathel"
print(fruits)
#5
del fruits[3]
print(fruits)
#6
print(fruits[-1])
#7
numbers=[1,2,3,4,5,6,7]
print(numbers[2:5])
#8
countries = [ "UK", "Canada", "Australia", "Germany"]
countries_new = countries.copy()
print("Original list:", countries)
print("Copied list:", countries_new)
#9
#looping through the list
for item in countries:
    print(item)
#10
Animals=["cow","cat","goat","horse"]   
Animals.sort()
print(Animals)
Animals.sort(reverse=True)
print(Animals)
#11
a_Animals=[]
for Animal in Animals:
   if "a" in Animal.lower():
        a_Animals.append(Animal)

print("Animals with 'a':")
for Animal in a_Animals:
    print(Animal)
    #12
#first_name = ['mary', 'vanessa',]
#last_name= ['nansumba','nak']
#joined_list = first_name + last_name

#print(joined_list) 
#Tuples
x=("samsung","iphone","tecno","redmi")
#print("my favorite brand is",x[1])
#2
second_last= x[-2]
#print(second_last)
#3
my_list=list(x)
my_list[1]="itel"
x=tuple(my_list)
#print("the new tuple is",x)
#4
my_list=list(x)
my_list.append("Huawei")
x=tuple(my_list)
#print("the new tuple is",x)
#5
#for item in x:
   # print(item)
#6
new_tuple =x[1:]
#print(new_tuple)
#7
cities=tuple(['Kampala',"Jinja","kasangati","kawanda"])
#print(cities)
#8
a,b,c ,d= cities
#print(b)
#print(c)
#print(d)
#9
#print(cities[1:4])
#10
first_name = ['mary', 'vanessa',]
last_name= ['nansumba','nak']
combined = first_name,last_name
#print(combined)
#11
colors=("black", "red", "green", "yellow")
result=(colors*3)
#print(result)
#12
thistuple =(1,3,7,8,7,5,4,6,8,5)
#count_8 =thistuple.count(8)
#print(count_8)
#Sets
#1
bev={"water","soda","juice"}
#2
bev.add("honey")
bev.add("fanta")
#print(bev)
#3
mySet ={"oven","kettle","microwave","refrigator"}
#print("microwave"in mySet)
#4
mySet.remove("kettle")

#print(mySet)
#5
#for item in mySet:
    #print(item)
#6
set= {1,2,3,4}
list1=[5,6]
set.update(list1)
#print(set)
#7
age={11,12,13}
names={"vanessa","mary","van"}
new= age.union(names)
#print(new)

#Strings
#1
x= "vanessa"
y=20
joined = str(y)+x
#print (joined)
#2
txt= "   Hello,  Uganda!"
stripped =txt.strip()
#print(stripped)
#3
uppercase = txt.upper()
#print(uppercase)
#4
changed = txt.replace("U","V")
#print(changed)
#5
y="Iam proudly Ugandan"
range_txt= y[1:4]
#print(range_txt)
#6
x='ALL"Data Scientists" are cool!"'
#print(x)


#(Dictionaries)
#1
#Shoes = {
#"brand" : "Nick",
#"color" : "black",
 #"size" : 40
#}
#print(Shoes["size"])
#2
#Shoes["brand"]="Adidas"
#print(Shoes)
#3
#Shoes["type"]="sneakers"
#print(Shoes)
#4
#keys =Shoes.keys()
#print(keys)
#5
#values=Shoes.values()
#print(values)
#6
#if "size" in Shoes:
    #print("size is present")
#7
#for item in Shoes:
    #print(item)
#8
#Shoes.__delitem__("color") 
#print(Shoes) 
#9
#Shoes.clear()
#print(Shoes)
#10
#new_dictionary={
    #"name": "nansumba",
    #"age": 20,
    #"favorites":"singing"
#}
#dictionary=new_dictionary.copy()
#print(dictionary)
#print(new_dictionary)
#11

#my_dict = {
    #"person1": {
      # "name": "John",
        #"age": 30,
        #"city": "New York"
   # },
    #"person2": {
       # "name": "Jane",
       # "age": 25,
       # "city": "Los Angeles"
    #}}
#print(my_dict)
