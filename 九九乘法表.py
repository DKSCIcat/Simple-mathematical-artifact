def main():
    t_sign=chr(0xD7)
    for i in range(1,10):
        for j in range(1,10):
            if i>=j:
                print(j,t_sign,i,"=",i*j,' ',end='')
        print('\n')

main()
if __name__ == "main":
    print("九九乘法表")
