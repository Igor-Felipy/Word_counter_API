from . import controllers
from flask import request, jsonify


@controllers.route("/", methods=["POST"])
def answer():
    text_old = request.json
    text = text_old["text"]
    text_cleared = clean_text(text)
    count_dict = counter(text_cleared)
    return jsonify(count_dict)



def clean_text(text):
    pontuation = [".",",",":","'",'"',"{","}","[","]","/",";","-","(",")","_","*","?","+",">","<","=","%","$","@","!","&","#"]
    new_text = "".join(c for c in text if c not in pontuation).upper()
    list = new_text.split()
    return list

def counter(list):
    count = dict()
    for n in list:
        count[n] = count.get(n,0)+1
    return count