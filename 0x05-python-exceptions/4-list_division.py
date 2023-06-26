#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list3 = []
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            value = 0
            print("division by 0")
        except IndexError:
            value = 0
            print("out of range")
        except TypeError:
            value = 0
            print("wrong type")
        except Exception as er:
            pass
        finally:
            my_list3.append(value)
    return my_list3
