import sender_stand_request
import data



def test_endpoint():

    request = sender_stand_request.post_new_kit(data.my_kit)
    print(request)



