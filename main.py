def main():
    ##################################################
    # Comlete your code here
    Male = int(input())
    Female = int(input())
    Total = Male+Female
    print('The total number of students:{0:10d}'.format(Total))
    print('The numberof males and females:{0:>8d} {1:>8d}'.format(
        Male, Female))
    print('The percentage of males and females:{0:.2%} {1:.2%}'.format(
        Male/Total, Female/Total))

    ##################################################
    pass


if __name__ == '__main__':
    main()
