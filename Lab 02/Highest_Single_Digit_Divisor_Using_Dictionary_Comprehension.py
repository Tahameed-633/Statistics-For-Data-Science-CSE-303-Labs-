result={
    i:max([d for d in range(2,9) if i%d==0],default=None)
    for i in range(1,1001)
}
print(result)
