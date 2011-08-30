# MobileFeed Controller
# =====================
#
# This file is part of MobileFeed.
#
# MobileFeed is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MobileFeed is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with MobileFeed.  If not, see <http://www.gnu.org/licenses/>.

import feedparser, flask, urllib
 
app = flask.Flask(__name__)

@app.template_filter('quote_plus')
def urlencode(s):
	return urllib.quote_plus(s)

@app.route('/')
def index():
	feeds = (('AfriGadget', 'http://feeds.feedburner.com/afrigadget'),
	         ('Danger Room', 'http://www.wired.com/dangerroom/feed/'),
	         ('Dutch News', 'http://www.dutchnews.nl/news/atom.xml'),
	         ('The Guardian', 'http://feeds.guardian.co.uk/theguardian/rss'),
	         ('Mashable', 'http://feeds.mashable.com/Mashable'),
	         ('MIH Media Lab', 'http://ml.sun.ac.za/feed/'),
	         ('ReadWriteWeb', 'http://feeds.feedburner.com/readwriteweb'),
	         ('TechCrunch', 'http://feeds.feedburner.com/techcrunch'),
	         ('The Technium', 'http://feeds.feedburner.com/thetechnium'),
	         ('Threat Level', 'http://www.wired.com/threatlevel/feed/'),
	         ('Ushahidi Blog', 'http://feeds.feedburner.com/ushahidi'),
	         ('White African', 'http://feeds.feedburner.com/white_african'),
	         ('Wired Top Stories', 'http://feeds.wired.com/wired/index'))
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
	entry = None

	for i in feed.entries:
		if i.id == entry_id:
			entry = i
	
	if entry == None:
		flask.abort(404)

	return flask.render_template('entry.html', feed_url=feed_url, feed=feed, entry=entry)

def main():
	app.debug = True
	app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
	main()
