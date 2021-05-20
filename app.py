from flask import Flask,render_template,request
import os
import requests
#from pprint import pprint as pp


#name = input(' >> ')
def getLastDate(name):
    URL = 'http://fow.kr/find/'+name
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36'}
    response = requests.get(URL)
    response = requests.get(URL,headers = headers)
    htmlt = response.text
    print(htmlt)
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
    print(result)
    return render_template('search.html',sum_name=sum_name,result=result)

print('end')

if __name__ == '__main__':
    app.run(debug=True)
