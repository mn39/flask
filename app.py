from flask import Flask,render_template,request
import os
import requests
#from pprint import pprint as pp


#name = input(' >> ')
def getLastDate(name):
    URL = 'http://fow.kr/find/'+name
    response = requests.get(URL)
    htmlt = response.text
    htmlt = htmlt.split("'tipsy_live' tipsy='")
    if(len(htmlt)>2):
        raw = htmlt[2][:19]
        return raw[:10]+':'+raw[11:]
    else:
        return 'No...'

##print(render_template('index.html'))

app = Flask(__name__, template_folder="views")
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/search')
def search():
    sum_name = request.args.get('name')
    result = getLastDate(sum_name)
    return render_template('search.html',sum_name=sum_name,result=result)

print('end')

if __name__ == '__main__':
    app.run(debug=True)
