if __name__ == "__main__":
    v=[12,24,53,2,52,64,39,20]
    #convert to set to remove duplicates
    s=set(v)
    s=sorted(s) #sorting the set
    print("The second largest element in v is: ",s[-2])
