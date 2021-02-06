from flask import Flask, request, jsonify, render_template, send_file
from pytube import YouTube
from flask_bootstrap import Bootstrap
import os
from flask_wtf import FlaskForm

app = Flask(__name__)
app.secret_key = 'the random string'
Bootstrap(app)


@app.route('/', methods=["POST", "GET"])
def index():
    # form = Link()
    # # name = form.name.data
    # # print(name)
    if request.method == "POST":
        youtube_link = request.form["youtubelink"]
        # print(youtube_link)
        return send_file(YouTube(youtube_link).streams.first().download(), as_attachment=True)
        # return render_template('home.html')
    else:
        return render_template('home.html')

# @app.route('/')
# def index():
#     return render_template('home.html')
#
#
# @app.route('/YouTube', methods=['post'])
# def postTesting():
#     name = request.form['youtubelink']
#
#     print(name)  # This is the posted value
#     return render_template('home.html'),200


# @app.route('/Youtube', methods=["POST"])
# def youtube():
#     # youtube_link_request = request.get_json(force=False, silent=False, cache=True)
#     # print(youtube_link_request)
#     youtube_link = request.form['name']
#     # downloads = youtube_link_request['path']
#     # print(downloads);
#     # path = "/Users/sameer/Documents/YouTube_mobile/YouTUBE_APP/backend/downloads"
#     yt = YouTube(youtube_link).streams.first().download()
#     views = YouTube(youtube_link).views
#     thumbnail = YouTube(youtube_link).thumbnail_url
#     title = YouTube(youtube_link).title
#     # streams_data = yt.streams.first().download()
#     # streams = []
#     # for stream in streams_data:
#     #     stream_info = stream
#     #     streams.append(stream_info.type)
#     return jsonify({"Data": "successful completed",
#                     "views": views,
#                     "thumbnail": thumbnail,
#                     "title": title,
#
#                     }), 200


if __name__ == "__main__":
    app.run(debug=True)
