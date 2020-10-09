from flask import Flask
from flask import request
import tmdbsimple as tmdb


app = Flask(__name__)
app.debug = True

tmdb.API_KEY = "72b2525e17e29bc72dc1d843de747c1f"

@app.route('/')
def user_input():
	html = ''
	html += '<html>\n'
	html += '<body>'
	html += '<form method="POST" action="search_results" />\n'
	html += 'Movie Search: <input type="text" name="user_search" />\n'
	html += '<p>\n </p>\n'
	html += '<input type="submit" value="Submit" />'
	return html

@app.route('/search_results', methods=['POST'])
def Result():
	search_input = request.form['user_search']
	Search_Func = tmdb.Search()
	reults_ = Search_Func.movie(query=search_input)
	html = ''
	html += '<html>\n'
	html += '<body>\n'
	html += '<style> table, th, td {border: 3px solid black; border-collapse: collapse;}'
	html += 'th, td {padding: 10px; text align: center;} </style>'
	html += '<Table>'
	html += '<tr><td>Movie</td><td>Information:</td></tr>'
	for i in Search_Func.results:
		pop_num = float(i['popularity'])
		release_num = str(i['release_date'])
		movie_ID = str(i['id'])
		image_link = "https://image.tmdb.org/t/p/w500" + i['poster_path']
		html += '<tr><th rowspan="4"><img src="' + image_link 
		html += '"style="width:150px;"></th>'
		html += '<td> Title:' + i['title'] + '</td></tr>'
		html += '<tr><td>Popularity:' + str(pop_num) + '</td></tr>'
		html += '<tr><td>Release Date:' + release_num + '</td></tr>'
		html += '<tr><td>Movie ID:' + movie_ID + '</td></tr>'
	html += '</Table>'
	html += '</html></body>'
	html += '<a href="/">Back</a>'
	return html


if __name__ == '__main__':
	app.run()
