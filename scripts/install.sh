#!/bin/bash
#
# MobileFeed Deployment Script
# ============================
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

# Update the sources.
apt-get update

# Upgrade the existing packages.
apt-get upgrade -y

# Install the necessary Debian packages.
apt-get install -y apache2 libapache2-mod-wsgi python-pip git

# Install the necessary Python packages.
pip install flask feedparser

# Create a user for MobileFeed processes to run as.
adduser --disabled-password --gecos "" mobilefeed

# Create a local clone of the application.
git clone https://github.com/charlvanniekerk/mobilefeed.git /var/www/mobilefeed

# Remove default Apache configuration.
rm -f /etc/apache2/sites-enabled/000-default

# Replace the default Apache configuration with the bundled one.
cp /var/www/mobilefeed/config/apache.conf /etc/apache2/sites-enabled/mobilefeed.conf

# Tell Apache to reload its configuration.
/etc/init.d/apache2 reload
