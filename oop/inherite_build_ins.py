class MyList(list):
    pass

def main():
    my_list = MyList()
    my_list.append('a')
    my_list.append('b')

    print(my_list[0])
    print(my_list[1])


if __name__ == "__main__":
    main()