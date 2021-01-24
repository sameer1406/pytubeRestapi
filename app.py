from flask import Flask, request, jsonify
from pytube import YouTube


app = Flask(__name__)


@app.route('/Youtube', methods=["POST"])
def youtube():
    youtube_link_request = request.get_json(force=False, silent=False, cache=True)
    print(youtube_link_request)
    youtube_link = youtube_link_request['link']
    # downloads = youtube_link_request['path']
    # print(downloads);
    yt = YouTube(youtube_link).streams.first().download()
    views = YouTube(youtube_link).views
    thumbnail = YouTube(youtube_link).thumbnail_url
    title = YouTube(youtube_link).title
    # streams_data = yt.streams.first().download()
    # streams = []
    # for stream in streams_data:
    #     stream_info = stream
    #     streams.append(stream_info.type)
    return jsonify({"Data": "successful completed",
                    "views": views,
                    "thumbnail": thumbnail,
                    "title": title,

                    }), 200


if __name__ == "__main__":
    app.run(debug=True)
