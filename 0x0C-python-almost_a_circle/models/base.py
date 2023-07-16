#!/usr/bin/python3
""" Module containing a class called Base"""
import json
import ast
import os
import csv


class Base:
    """ Base class is created """

    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor """

        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ converting a python object to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []

        string = json.dumps(list_dictionaries)
        return string

    @classmethod
    def save_to_file(cls, list_objs):
        """ saving JSON string to a file """
        file_name = f"{cls.__name__}.json"
        k = []
        with open(file_name, "w") as wf:
            if list_objs is None or len(list_objs) == 0:
                # Method 1
                # string = cls.to_json_string(None)
                # convert_string = ast.literal_eval(string)
                # or eval to convert '[]' into []
                # json.dump(convert_string, wf)
                # Method 2
                wf.write(cls.to_json_string(None))
            else:
                for i in list_objs:
                    j = cls.to_dictionary(i)
                    k.append(j)
                    # or we can use list comprehension:
                    # k = [i.to_dictionary() for i in list_objs]
                    # (time complexity 0)
                json.dump(k, wf)

    @staticmethod
    def from_json_string(json_string):
        """ converting a json string to python object """

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creating new instance with given attributes """
        if cls.__name__ == 'Square':
            new_in = cls(2)
        if cls.__name__ == 'Rectangle':
            new_in = cls(2, 2)
        new_in.update(**dictionary)
        return new_in

    @classmethod
    def load_from_file(cls):
        """ method that take input form a file
        and return a list of instances"""
        file_name = cls.__name__ + '.json'
        if not os.path.exists(file_name):
            return []
        with open(file_name, "r") as rf:
            string = rf.read()
        final_list = []
        list_obj = cls.from_json_string(string)
        for di in list_obj:
            new_in = cls.create(**di)
            final_list.append(new_in)
        return final_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        file_name = f"{cls.__name__}.csv"
        with open(file_name, "w") as wf:
            """ creating a csv writer object"""
            csv_writer = csv.writer(wf)
            if list_objs is None or len(list_objs) == 0:
                new_list = []
            else:
                for i in list_objs:
                    if cls.__name__ == 'Rectangle':
                        new_list = [i.id, i.width, i.height, i.x, i.y]
                    if cls.__name__ == 'Square':
                        new_list = [i.id, i.size, i.x, i.y]
                    csv_writer.writerow(new_list)

    @classmethod
    def load_from_file_csv(cls):
        file_name = cls.__name__ + '.csv'
        final_list = []
        if not os.path.exists(file_name):
            return []
        with open(file_name, "r") as rf:
            csv_reader = csv.reader(rf)
            for r in csv_reader:
                if cls.__name__ == 'Rectangle':
                    new_di = {"id": int(r[0]), "width": int(r[1]),
                              "height": int(r[2]), "x": int(r[3]),
                              "y": int(r[4])}
                if cls.__name__ == 'Square':
                    new_di = {"id": int(r[0]), "size": int(r[1]),
                              "x": int(r[2]), "y": int(r[3])}
                new_in = cls.create(**new_di)
                final_list.append(new_in)
        return final_list
