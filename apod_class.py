import requests, re, time
import simplejson as json
from PIL import Image
from io import BytesIO 
from DateListGen import daterange

url = 'https://api.nasa.gov/planetary/apod'
class REST_APOD():
    def __init__(self, date):
        payload = {'date': date, 'api_key': 'DEMO_KEY', 'hd': True} #Sign up and replace your own key with the DEMO KEY
        try:
            self.r = requests.get(url,payload)
        except Exception as error:
            print "Error: ", error
        else:
            self.body = json.loads(self.r.text)

    def verify_images(self):
        media_url = self.body['url']
        media_type = self.body['media_type']
        if media_type == 'image':
            print "[OK] -", media_url
            call.save_images(date)
        else:
            print "------------> [CHECK] -", media_url
            with open('/Users/rs-m91/Projects/NASA_API/Check.txt', 'a+') as check:
                check.write(media_url+'\n')

    def save_images(self,date):
        media_url = self.body['url']
        filename = re.search(r'(\w+\.\w+)$', media_url)
        r_image = requests.get(media_url)
        try:
            with Image.open(BytesIO(r_image.content)) as img:
                img.save('/Users/rs-m91/Projects/NASA_API/Pictures/{}_{}'.format(date,filename.group(1)))
        except Exception as error:
            print "Error: ", error
        else:
            print filename.group(1), 'created' def Rate_Remaining(self): headers = self.r.headers['X-RateLimit-Remaining'] print headers
        
        
        

for date in daterange('2018-05-11', '2018-06-01'):
    call = REST_APOD(date)
    call.verify_images()

call.Rate_Remaining()
