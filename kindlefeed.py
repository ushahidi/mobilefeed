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

@app.route('/feed')
def feed():
	data = feedparser.parse('http://feeds.feedburner.com/TechCrunch/')
	return flask.render_template('feed.html', data=data)

@app.route('/entry')
def entry():
	feed = feedparser.parse('http://feeds.feedburner.com/TechCrunch/')
	return flask.render_template('feed.html', feed=feed)

def main():
	app.debug = True
	app.run(host='0.0.0.0')

if __name__ == '__main__':
	main()
