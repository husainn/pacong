# list1 = [1,2,3,4,5]
# list1.pop(1)
# list1.insert(1,2)
# print(list1)

from urllib.parse import urlparse

link = "https://i2.chuimg.com/d1069cbb9b104e57aff215fda49c…008h.jpg?imageView2/1/w/150/h/90/interlace/1/q/90"
o = urlparse(link)
print(o,type(o))
print(o.path,dir(o))

