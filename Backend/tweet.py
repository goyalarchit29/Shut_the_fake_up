import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "W701fEkTxIMaqa9ka6QV5T05O",
    "consumer_secret"     : "hQOZp3hr3BacHK0SZNkP96Up7axQEGGwvid5GmHEt9CJLALlci",
    "access_token"        : "917868221709008896-ilWT2rXzl5GQOy13RwNQ93QtKvNV1lR",
    "access_token_secret" : "WHRJlVa7yV7QJhTNBJLzn13addmLil1srOWwYoYwnY8Nx" 
    }

  api = get_api(cfg)
  tweet = "Fuck, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
