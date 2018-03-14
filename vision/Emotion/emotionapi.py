import requests
import json
def getemotion() :
    json_resp = requests.post( 'https://api-face.sightcorp.com/api/detect/',
              data  = { 'app_key' : 'e00f8c8746bf4b01b3f33b476cbf1e74' },
              files = { 'img'     : ( 'filename', open( '/home/pi/Desktop/ReactionBot2.0/vision/Emotion/picam.jpg', 'rb' ) ) } )

    #print (json_resp.text)
    apiresp =json.loads(json_resp.text)
    for person in apiresp['people']:
        onlyemotion=(person['emotions'])
#for key,val in onlyemotion.items():
 #       exec(key + '=val')

#del onlyemotion["surprise"]
#del onlyemotion["disgust"]

    #print (onlyemotion)

        finalemotion = max(onlyemotion, key=lambda i: onlyemotion[i])
        return(finalemotion)


#if emotion == "happiness":

#print (max(onlyemotion.items(), key=operator.itemgetter(1))[0])
# emotionarray[0]=happiness
# emotionarray[1]=sadness
# emotionarray[2]=anger
# emotionarray[3]=fear
# maxval=emotionarray[0]
# for k in range(1,3) :
#     if maxval<emotionarray[k] :
#         maxval=emotionarray[k]
# for i in range(0,3) :
#     if maxval==emotionarray[i] :
#         break

# print(i)
