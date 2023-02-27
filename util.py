def find_address(loc=str):

    with open('OriginEntry.txt', 'r') as origin:
        for line in origin:

            if loc == line[:6]:
                address = line[6:].replace('\t', ' ').replace('\n', ' ')
                return address.strip()


def container_info(container):
    box = container[12]
    loc_key = container[54:60]
    discount_key = container[49]
    qty = int(container[200:207])
    address = find_address(loc_key)

    dic = dict()

    dic = {
        'box': box,
        'loc_key': loc_key,
        'discount_key': discount_key,
        'qty': qty,
        'address': address
    }

    return dic


def get_containers():

    containers = []

    with open('maildat.csm', 'r') as maildat:
        for container in maildat:
            containers.append(container_info(container))

    return containers


def get_locations():
    locations = set()
    containers = get_containers()


    for container in containers:

        locations.add(find_address(container['loc_key']))

    return locations
            