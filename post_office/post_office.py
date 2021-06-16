def group(parts, k):
    parts.sort(reverse=True)
    avg=sum(parts)/k
    truck_no=1
    part_no=0
    while truck_no<=k and truck_no<=k:
        load=[]
        load_sum=0
        while load_sum<avg and part_no<len(parts):
            load.append(parts[part_no])
            load_sum+=parts[part_no]
            part_no+=1
        print("Trick #{}: ".format(truck_no)+" ".join([str(part) for part in load]))
        truck_no+=1

if __name__=='__main__':
    k=int(input("Enter count of trucks: "))
    parts=list(map(int,input("Enter parts weight: ").split()))
    group(parts, k)
