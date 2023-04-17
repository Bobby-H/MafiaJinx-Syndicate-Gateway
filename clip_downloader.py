import requests
import configparser
import twitch #<< go through pip install history in terminal "--user twitch-python"
# and search for twitch libs that have a method like get_clips_for_broadcaster. runtime error related to how im importing 
# this twitch library.
import twitch.helix as helix
import twitch.v5 as v5

config = configparser.ConfigParser()

client_secret = config['client_secret']
client_id = config['client_id']
oauth_token = config['oauth_token']
access_token = config['access_token']
broadcaster_id = config['broadcaster_id']
clip_limit = 10

# Connect to the Twitch API
helix = twitch.Helix(access_token, client_id, oauth_token)

# Get the most recent clips for the specified broadcaster
clips = helix.clips.get_clips_for_broadcaster(broadcaster_id=broadcaster_id, first=clip_limit)

# Loop through the clips and download them
#for clip in clips:
clip_url = clip.thumbnail_url.replace('-preview.jpg', '.mp4')
response = requests.get(clip_url)
#    with open(f'{clip.id}.mp4', 'wb') as f:
#        f.write(response.content)

for user, clips in helix.users('MafiaJinx'), clips(first=5):
    with open(f'{clip.id}.mp4', 'wb') as f:
        f.write(response.content)