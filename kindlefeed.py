# KindleFeed Controller
# =====================
#
# This file is part of KindleFeed.
#
# KindleFeed is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# KindleFeed is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with KindleFeed.  If not, see <http://www.gnu.org/licenses/>.

import feedparser, flask, urllib
 
app = flask.Flask(__name__)

@app.template_filter('quote_plus')
def urlencode(s):
	return urllib.quote_plus(s)

@app.route('/')
def feed():
	feeds = ({'title': 'TechCrunch', 'url': 'http://feeds.feedburner.com/techcrunch'})
	return flask.render_template('index.html', feeds=feeds)

@app.route('/feed')
def feed():
	url = flask.request.args.get('url')
	feed = feedparser.parse(url)
	return flask.render_template('feed.html', url=url, feed=feed)

@app.route('/entry')
def entry():
	feed_url = flask.request.args.get('feed')
	entry_id = flask.request.args.get('entry')
	feed = feedparser.parse(feed_url)

	for i in feed.entries:
		if i.id == entry_id:
			entry = i

	return flask.render_template('entry.html', feed_url=feed_url, feed=feed, entry=entry)

def main():
	app.debug = True
	app.run(host='0.0.0.0')

if __name__ == '__main__':
	main()
