L=[]
clients=[]
with open('zamowienia.csv' , 'r') as f:
    first_line = f.readline()
    for line in f:
        line = line.strip().split(";")
        L.append(line[2])
        clients.append(line[1])
#task1: which day was the most popular with orders
#version1  
def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i   
    return num 
#print(most_frequent(L)) 

#version2
import statistics 
from statistics import mode 
def most_common(List): 
    return(mode(List))
#print(most_common(L))

    
print('task1, most_popular_day',most_frequent(L))


#task2: how many customers used a discount code
i=0
with open('zamowienia.csv', 'r') as s:
    first_line = s.readline()
    for line in s:
        line = line.strip().split(";")
        if line[3] !='':
            i+=1
            #print('task2, with discount:',line,i)



#task3 how many customers ordered more than once
print('task3',len(sorted(set([i for i in clients if clients.count(i)>1]))))

#task4
#a) which product was most popular
#b) how many customers bought this product with discount

#version1
items=[] # list of all products from wyslane.csv
with open('wyslane.csv' , 'r') as g:
    first_line = g.readline()
    for line in g:
        line = line.strip().split(";")
        for column in range(1,len(line)):
        
            if line[column] =='':
                pass
            else:
                items.append(line[column])
def most_common(List): 
    return(mode(List))
#print(most_common(items))
#version2
def most_frequent(List): 
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(List): 
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count : 
            count, itm = dict[item], item 
    return(itm) 
mpi=most_frequent(items)    
print('task4a,most_popular_item',mpi)

#task4b
order_id=[] #list of order ids for the most popular product 
with open('wyslane.csv' , 'r') as h:
    first_line = h.readline()
    for line in h:
        line = line.strip().split(";")
        #print(line[1])
        for column in range(1,len(line)):
            if line[column]==mpi:
                order_id.append(line[0])
    #print(order_id)
#order id must be on the list odrer_id and must include the word KUPON musi byc na liscie order_id oraz musi miec KUPON
i=0
for line in open("zamowienia.csv"):
    line = line.strip().split(";")
    if line[3] !='' and line[0] in order_id:
        i+=1
        print('task4b',line,i)

#task5 which product was most popular among products bought with the discount
#idea: to find ids of all products with discounts in zamowienia.csv, they will be stored on the list WithDiscount, then I will search wyslane.csv and if order_id will match the one on the list WithDiscount and  line[1],line[2], line[3] != NULL, then products line[1],line[2],line[3] will be added to the list ProductsWithDiscount and finally the most popular will be found on this list
WithDiscount=[]
with open('zamowienia.csv' , 'r') as k:
    first_line = k.readline()
    for line in k:
        line = line.strip().split(";")
        if line[3] !='':
            WithDiscount.append(line[0])

ProductsWithDiscount=[]
with open('wyslane.csv' , 'r') as l:
    first_line = l.readline()
    for line in l:
        line = line.strip().split(";")
        if line[0] in WithDiscount:
            ProductsWithDiscount.append(line[1])
        if line[0] in WithDiscount and line[2] !='':
            ProductsWithDiscount.append(line[2])
        if line[0] in WithDiscount and line[3] !='':
            ProductsWithDiscount.append(line[3])

print('task5',most_common(ProductsWithDiscount))

#task6
WithoutDiscount=[] #list order_id of products without discount 
d={} # with discount {order_id1 : 0.15, order_id2 : 0.30...}
with open('zamowienia.csv' , 'r') as k:
    first_line = k.readline()
    for line in k:
        line = line.strip().split(";")
        if line[3] =='':
            WithoutDiscount.append(line[0])
        else:
            d[line[0]]= int(line[3].rstrip("%"))/100

#print(d.values())

itemsWithoutDiscount=[] # item_id wyslanych produktow bez znizki
#d2={}
with open('wyslane.csv' , 'r') as g:
    first_line = g.readline()
    for line in g:
        line = line.strip().split(";")
        if line[0] in WithoutDiscount:
            itemsWithoutDiscount.append(line[1])
        elif line[2] !='' and line[0] in WithoutDiscount:
            itemsWithoutDiscount.append(line[2])
        elif line[3] !='' and line[0] in WithoutDiscount:
            itemsWithoutDiscount.append(line[3])
g.close()

#three dicts for each column in the form {item_id:order_id} for those order_id's which are in d with discount
d2={}
with open('wyslane.csv' , 'r') as h:
    first_line = h.readline()
    for line in h:
        line = line.strip().split(";")  
        if line[0] in d.keys():
            d2[line[1]] = d[line[0]] 
h.close()

d3={}
with open('wyslane.csv' , 'r') as j:
    first_line = j.readline()
    for line in j:
        line = line.strip().split(";")     
        if line[0] in d.keys() and line[2] !='':
            d3[line[2]] = d[line[0]] 
j.close()

d4={}
with open('wyslane.csv' , 'r') as k:
    first_line = k.readline()
    for line in k:
        line = line.strip().split(";") 
        if line[0] in d.keys() and line[3] !='':
            d4[line[3]] = d[line[0]]
#print(len(d2), 'd2', len(d3), 'd3', d4,'d4')

#each dictionary into list [base_price*discount,base_price2*0.40]
L2=[]
L3=[]
L4=[]
with open('cena bazowa.csv' , 'r') as l:
    first_line = l.readline()
    for line in l:
        line = line.strip().split(";") 
        if line[0] in d2.keys():
            L2.append(float(line[1])*d2[line[0]])

print('sum_d2',sum(L2))    

with open('cena bazowa.csv' , 'r') as m:
    first_line = m.readline()
    for line in m:
        line = line.strip().split(";") 
        if line[0] in d3.keys():
            L3.append(float(line[1])*d3[line[0]])

print('suma_d3',sum(L3)) 
    
with open('cena bazowa.csv' , 'r') as n:
    first_line = n.readline()
    for line in n:
        line = line.strip().split(";") 
        if line[0] in d4.keys():
            L4.append(float(line[1])*d4[line[0]])

print('sum_d4',sum(L4)) 
print('price with discount',sum(L4)+sum(L3)+sum(L2)) 

PriceWithoutDiscount=[] 
with open('cena bazowa.csv' , 'r') as m:
    first_line = m.readline()
    for line in m:
        line = line.strip().split(";")
        if line[0] in itemsWithoutDiscount:
            PriceWithoutDiscount.append(line[1])
    #print(PriceWithoutDiscount)

PriceWithoutDiscount = list(map(int, PriceWithoutDiscount))   
print('Price without discount',sum(PriceWithoutDiscount)) 
print('task6, all together', sum(PriceWithoutDiscount)+sum(L4)+sum(L3)+sum(L2))   
