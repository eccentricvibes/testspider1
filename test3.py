from pyquery import PyQuery as pq


# doc = pq(html)
# li_content = doc("#container .list li")
# print(type(li_content))
# for l in li_content.items():
#     print(l.text())

html = """
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
"""

doc = pq(html)
li = doc('.list li a')
print(li.html())
# li.addClass("aiyc")
# print(li)

# for i in li.items():
#     print(li.find("a"))

# for i in li.items():
#     print(i.text())
#     print(i.attr("href"))
# doc = pq(html)
# items = doc(".list")
# print(type(items))
# print(items)
#
# lis = items.parent()
# for i in lis.items():
#     print(i.text())
# print(type(items))
# print(items)

# lis = items.children(".active")
# for i in lis.items():
#     print(i.text())
# # print(type(lis))    
# # print(lis)

# lis = items.parent(".active")
# container = items.parent()
# for i in items.parent():
#     print(i)
# print(type(container))
# print(container)