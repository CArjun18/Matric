import csv

def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

read_csv("products.csv") 

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        print(f"Total word count: {len(words)}")


count_words("info.txt")  


import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        print(data)
        return data


read_json("company.json") 