from django.shortcuts import render
from django.utils.safestring import mark_safe
import json



def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


# import paralleldots
#
#
# def do_sentiment_analysis(request):
#     user_sent = ""
#     user_input = ""
#     fname = "na"
#     if request.POST:
#         user_input = request.POST.get('user_input', '')
#         lang_code = "en"
#         paralleldots.set_api_key("XXXXXXXXX")
#         user_response = paralleldots.sentiment(user_input, lang_code)
#         user_sent = user_response['sentiment']
#
#         if (user_sent == 'neutral'):
#             fname = "emoticon-1634586_640.png"
#         elif (user_sent == 'negative'):
#             fname = "emoticon-1634515_640.png"
#         elif (user_sent == 'positive'):
#             fname = "smiley-163510_640.jpg"
#         else:
#             fname = "na"
#
#     return render(request, 'room.html', {'resp': user_sent, 'fname': fname, 'user_input': user_input})
