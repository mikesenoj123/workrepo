from util import *
import collections


# Dropship class object
class dropship_report:
    def __init__(self, address, qty, pallets, emm, one_foot, mm):
        self.address = address
        self.qty = qty
        self.pallets = pallets
        self.emm = emm
        self.one_foot = one_foot
        self.mm = mm

    def show_weight(self):
        weight = round((self.pallets * 20) + (self.emm * 2.3) + (self.one_foot * 1.3) + (self.mm * 2))
        return f'Weight in pounds: {weight}'

    def __str__(self):
        return f'\naddress: {self.address} \nqty: {self.qty}, pallets: {self.pallets}, EMM: {self.emm}, one_foot: {self.one_foot}, MM: {self.mm}'
        
dropship_reports = []



locations = get_locations()
containers = get_containers()
    

qty = 0
emm_count = 0
one_count = 0
mm_count = 0
pallets = 0
pallets_qty = 0
count = 0


for loc in locations:

    for container in containers:

        if container['address'] == loc:

            if container['box'] == 'P':
                pallets = pallets + 1
                pallets_qty = container['qty']

            elif container['box'] == 'E':
                emm_count = emm_count + 1
                qty = qty + container['qty']

            elif container['box'] == 'O':
                one_count = one_count + 1
                qty = qty + container['qty']
                
            elif container['box'] == 'M':
                mm_count = mm_count + 1
                qty = qty + container['qty']
        else: 
            continue

    dropship_reports.append(dropship_report(address=loc, qty=qty, pallets=pallets, emm=emm_count, mm=mm_count, one_foot=one_count))


count = 1


for drop in dropship_reports:
    print(f'Drop: {count}')
    count = count + 1
    print(drop)
    print(drop.show_weight())
    print()