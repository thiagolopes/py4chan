import requests
import py4chan
from flask import Flask, render_template


app = Flask('py4chan')

context_chan = requests.get('https://4chan.org')
context_chan_text = context_chan.text


@app.route('/')
def boards():
    boards = py4chan.get_boards(context_chan_text, just_code=True)
    return render_template('index.html', boards_list=boards)


@app.route('/<string:board>/')
def threads(board=None):
    try:
        context = requests.get('https://4chan.org/{}'.format(board))
        context.raise_for_status()
        threads = py4chan.get_threads(context.text)
        return render_template('threads.html', threads=threads)
    except requests.exceptions.HTTPError:
        return "404, no threads here", 404


@app.route('/<string:name>/<int:id_t>/')
def thread_images(name=None, id_t=None):
    try:
        context = requests.get('https://boards.4chan.org/{}/thread/{}'
                               .format(name, id_t))
        context.raise_for_status()
        images = py4chan.get_images_links(context.text)
        return render_template('images.html', images_list=images)
    except requests.exceptions.HTTPError:
        return "404, no images here", 404


if __name__ == '__main__':
    app.run(debug=True)
