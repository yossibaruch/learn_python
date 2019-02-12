import netaddr

print("""
This script will:
1. Input of CIDR format (a.b.c.d/Y) will be translated to IP range (A.B.C.D - E.F.G.H)
2. Input of CIDR format with IP address (a.b.c.d/Y A.B.C.D) will get the response of ('Address A.B.C.D is [NOT] within CIDR a.b.c.d/Y)
""")

address = input("Write down 'CIDR' or 'CIDR IP':\n")

if ' ' in address:
    CIDR_Format, address = address.split(' ')
    if address in netaddr.IPNetwork(CIDR_Format):
        print(f'Address {address} is within given CIDR: {CIDR_Format}')
    else:
        print(f'Address {address} is NOT!!! within given CIDR: {CIDR_Format}')
else:
    CIDR_Format = address

print("IP range is: ", netaddr.IPNetwork(CIDR_Format)[0], "-", netaddr.IPNetwork(CIDR_Format)[-1])
