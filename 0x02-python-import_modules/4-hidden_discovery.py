#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hid_list = dir(hidden_4)
    for name in hid_list:
        if name[0] + name[1] != "__":
            print("{}".format(name))
