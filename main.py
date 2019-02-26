import twitter
import os
import json
import logging

log = logging.log()


tweet_folder = 'C:\dev\\twitter_app\\tweets'
API_KEY = 'LoQsh0jrgYULN3hErc8tZVkPW'
API_SECRET_KEY = 'Q8zDpyMdOPRfZgcEPSmOEelp81C0q0JneAz5k2wniNHPlx0sCU'
ACCESS_TOKEN = '1601882004-H6hVPZvUmn9DxsRSKkny2T9xX5CaocIY5cG97eM'
ACCESS_TOKEN_SECRET = 'IpzQTCECFKhH203UTSJZi3PY61s4BgURKXzOuDi7cQsHi'
DEFAULT_AUTH_ARRAY = [API_KEY,API_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET]


def get_dump_path():
    output_filename = os.path.join('C:\dev\\twitter_app\\tweets', 'python_tweets.json')
    print 'output path: {0}'.format(output_filename)
    return output_filename


def get_labels_path():
    output_filename = os.path.join('C:\dev\\twitter_app\\tweets', 'python_classes.json')
    print 'output path: {0}'.format(output_filename)
    return output_filename


def get_auth(auth_array=None):
    auth_array = auth_array or DEFAULT_AUTH_ARRAY
    authorization = twitter.OAuth(*auth_array)
    print 'log: {0}'.format(authorization)
    return authorization


def populat_tweet_dump():
    authorization = get_auth()
    output_filename = get_dump_path()
    t = twitter.Twitter(auth=authorization)
    with open(output_filename, 'a') as output_file:
        search_results = t.search.tweets(q="python", count=100)['statuses']
        for tweet in search_results:
            if 'text' in tweet:

                print

                output_file.write(json.dumps(tweet))
        output_file.write("\n\n")
    print


def cleaner():
    tweets = list()
    input_filename = get_labels_path()
    with open(input_filename) as inf:
        for line in inf:
            if len(line.strip()) == 0:
                continue
        tweets.append(json.loads(line))















if __name__ == '__main__':
    populat_tweet_dump()
    print
