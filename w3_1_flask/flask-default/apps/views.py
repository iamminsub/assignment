from flask import render_template, Flask, request
#from apps import app

app = Flask(__name__)
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	get = None
	google = ''
	naver = ''
	daum = ''
	if request.args:
		get = request.args['text_get']
		naver = "http://search.naver.com/search.naver?where=nexearch&query="+ get +"&sm=top_hty&fbm=1&ie=utf8"
		google = "https://www.google.co.kr/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#newwindow=1&q=" + get
		daum = "http://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&o=&q="+ get
	return render_template("index.html", variable_get = get, variable_get_google = google, variable_get_naver = naver, variable_get_daum = daum)

if __name__ == "__main__":
	app.run(port = 5002)