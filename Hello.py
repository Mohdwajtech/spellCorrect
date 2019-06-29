from flask import Flask, render_template, request
import split

from spellchecker import SpellChecker

spell = SpellChecker()
app = Flask(__name__, template_folder = 'template')

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        
       
        pro = spell.word_probability(spell.correction(result['Word']))
        if (pro !=0):
             a={spell.correction(result['Word']):spell.word_probability(spell.correction(result['Word']))}
        else:
            a = {}
        print('a : ',a)
        print("pro:",pro)
        b=list(spell.candidates(result['Word']))
        
        print('b :',b)
        
        b_={}
        print('len:',len(b))
        if (len(b)==1):
            print('b[0] :',b[0])
            print('probab :',spell.word_probability(b[0]))
            if(spell.word_probability(b[0])!=0.0):
                b_[b[0]]=spell.word_probability(b[0])
            else:
                b_={'None':0.0}
        else:
        
            for i in b:
                b_[i]=spell.word_probability(i)
        
        print('b_ : ',b_)
        
        c=split.viterbi_segment(result['Word'])[0]
        print('c :',c)
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
        
        print('c :',c_)
        
        return render_template("result.html",  likely=a, suggest=b_,splitted=c_, word = result['Word'].upper())
    
if __name__ == '__main__':
    app.run(debug = True)