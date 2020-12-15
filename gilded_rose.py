# -*- coding: utf-8 -*-
from tkinter import *

top=Tk()
Items = []
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        i =0
        for item in self.items:
            i+=1
            if item.quality != 0:
                if item.quality == 50 and item.name != 'Sulfuras':
                    item.sell_in-=1
                    if item.sell_in < 0:
                        item.sell_in = 0
                    continue
                else:
                    if item.sell_in != 0:
                        if item.name == 'Base':
                            item.quality -= 1
                        elif item.name == 'Aged Brie':
                            item.quality += 1

                        elif item.name == 'Backstage passes':
                            if item.sell_in <= 10 and item.sell_in > 5:
                                item.quality += 2
                            elif item.sell_in <= 5:
                                item.quality += 3
                            else:
                                item.quality -= 1
                        elif item.name == 'Conjured':
                            item.quality -= 2
                    else:
                        if item.name == 'Sulfuras':
                            continue
                        elif item.name == 'Backstage passes':
                            item.quality = 0
                        elif item.name == 'Conjured':
                            item.quality -= 4
                        else:
                            item.quality -= 2

                    item.sell_in -= 1

                    if item.sell_in < 0:
                        item.sell_in = 0

            else:
                item.sell_in-=1

                if item.sell_in < 0:
                    item.sell_in = 0

            if item.quality > 50 and item.name != 'Sulfuras':
                item.quality=50
            if item.quality<0:
                item.quality=0




            #print(item)
            #print(i)

        Items=self.items

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


f=0
# appending instances to list
Items.append(Item('Aged Brie', 30, 25))
Items.append(Item('Sulfuras', 30, 80))
Items.append(Item('Backstage passes', 30 , 25))
Items.append(Item('Conjured', 30 , 25))
Items.append(Item('Base',30,25))

def update():
    system = GildedRose(Items)
    system.update_quality()
    w = Text(top, width=15, height=4)
    w.grid(row=1, column=0)
    w.insert(END, "Item name")
    w = Text(top, width=15, height=4)
    w.grid(row=1, column=1)
    w.insert(END, "sell in")
    w = Text(top, width=15, height=4)
    w.grid(row=1, column=2)
    w.insert(END, "quality")

    for x in range(len(Items)):
        w = Text(top, width=15, height=2)
        w.grid(row=x + 2, column=0)
        w.insert(END, Items[x].name)
        w = Text(top, width=15, height=2)
        w.grid(row=x + 2, column=1)
        w.insert(END, Items[x].sell_in)
        w = Text(top, width=15, height=2)
        w.grid(row=x + 2, column=2)
        w.insert(END, Items[x].quality)

    top.mainloop()
def show():
    w = Button(text='show', command=update)
    w.grid(row=0, column=1)
    top.mainloop()


w = Text(top, width=15, height=4)
w.grid(row=1, column=0)
w.insert(END, "Item name")
w = Text(top, width=15, height=4)
w.grid(row=1, column=1)
w.insert(END, "sell in")
w = Text(top, width=15, height=4)
w.grid(row=1, column=2)
w.insert(END, "quality")

for x in range(len(Items)):
    w = Text(top, width=15, height=2)
    w.grid(row=x + 2, column=0)
    w.insert(END, Items[x].name)
    w = Text(top, width=15, height=2)
    w.grid(row=x + 2, column=1)
    w.insert(END, Items[x].sell_in)
    w = Text(top, width=15, height=2)
    w.grid(row=x + 2, column=2)
    w.insert(END, Items[x].quality)

show()