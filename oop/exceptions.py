
def main():
    try:
        pass;
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except TypeError:
        print("TypeError")
        raise
    except Exception as e:
        print(e.__class__.__name__)
    else:
        print("There is no exception")
    finally:
        print("Always execute whether this is an expception")

if __name__ == '__main__':
    main()