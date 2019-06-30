from flask import Flask, render_template, request
import split
from spellchecker import SpellChecker
import random
import string

num = random.randint(3,5)
letters = string.ascii_lowercase

spell = SpellChecker()
app = Flask(__name__, template_folder = 'template')

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
    elif request.method == 'GET':
        randm =""
        randm ="".join(random.choice(letters) for i in range(num))
        result={}
        result['Word'] = randm
       
    pro = spell.word_probability(spell.correction(result['Word']))
    if (pro !=0):
         a={spell.correction(result['Word']):spell.word_probability(spell.correction(result['Word']))}
    else:
        a = {}
    b=list(spell.candidates(result['Word']))
    b_={}
    if (len(b)==1):
        if(spell.word_probability(b[0])!=0.0):
            b_[b[0]]=spell.word_probability(b[0])
        else:
            b_={'None':0.0}
    else:
        for i in b:
            b_[i]=spell.word_probability(i)

    c=split.viterbi_segment(result['Word'])[0]
    c_={}
    cc=[]
    for i in c:
        if len(i)>2:
            cc.append(i)
    if len(cc)>1:
        for i in cc:
                c_[i]=spell.word_probability(i)
    else:
        c_={'None':0.0}
    return render_template("result.html",  likely=a, suggest=b_,splitted=c_, word = result['Word'].upper())
    
if __name__ == '__main__':
    app.run(debug = True)
