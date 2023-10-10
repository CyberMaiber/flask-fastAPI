import requests
import json
import datetime

url = 'http://127.0.0.1:8000/customers/'

customer1 = {'name':'Vasya','email':'123@567.ru','surname':'Ivanov','password':'somepass'}
customer2 = {'name':'Fedia','email':'fp@567.ru','surname':'Petrov','password':'somepass'}
customer3 = {'name':'Petr','email':'pf@567.ru','surname':'Fedorov','password':'somepass'}
customer4 = {'name':'Fedor','email':'fv@567.ru','surname':'Vasiliev','password':'somepass'}
customer5 = {'name':'Evgen','email':'eo@567.ru','surname':'Onegin','password':'somepass'}

print(requests.post(url,data=json.dumps(customer1)).content)
print(requests.post(url,data=json.dumps(customer2)).content)
print(requests.post(url,data=json.dumps(customer3)).content)
print(requests.post(url,data=json.dumps(customer4)).content)
print(requests.post(url,data=json.dumps(customer5)).content)

customer1 = {'name':'Vasya','email':'123@567.ru','surname':'Ivanov','password':'anotherpass'}
print(requests.put(url + '1',data=json.dumps(customer1)).content)

url = 'http://127.0.0.1:8000/goods/'

good1 = {'name':'gorshok','description':'very big gorshok','price': 123.01}
good2 = {'name':'vaza','description':'very big vaza','price': 124.02}
good3 = {'name':'taz','description':'very big taz','price': 125.03}
good4 = {'name':'picture','description':'very big picture','price': 126.04}
good5 = {'name':'polka','description':'very big polka','price': 127.05}

print(requests.post(url,data=json.dumps(good1)).content)
print(requests.post(url,data=json.dumps(good2)).content)
print(requests.post(url,data=json.dumps(good3)).content)
print(requests.post(url,data=json.dumps(good4)).content)
print(requests.post(url,data=json.dumps(good5)).content)

good1 = {'name':'gorshok','description':'very big gorshok','price': 99.01}
print(requests.put(url + '1',data=json.dumps(good1)).content)

url = 'http://127.0.0.1:8000/orders/'

order1 = {'customer_id':1,'goods_id':5,'order_date': "2023-12-08",'status':'в обработке'}
order2 = {'customer_id':2,'goods_id':4,'order_date': "2023-11-09",'status':'в обработке'}
order3 = {'customer_id':3,'goods_id':3,'order_date': "2023-10-10",'status':'в обработке'}
order4 = {'customer_id':4,'goods_id':2,'order_date': "2023-09-11",'status':'в обработке'}
order5 = {'customer_id':5,'goods_id':1,'order_date': "2023-08-12",'status':'в обработке'}

print(requests.post(url,data=json.dumps(order1)).content)
print(requests.post(url,data=json.dumps(order2)).content)
print(requests.post(url,data=json.dumps(order3)).content)
print(requests.post(url,data=json.dumps(order4)).content)
print(requests.post(url,data=json.dumps(order5)).content)
