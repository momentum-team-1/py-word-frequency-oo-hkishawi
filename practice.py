# class Tweet:
#     pass

# a = Tweet()
# b = Tweet()
# a.message = '140 characters'
# b.message = "testing second message"
# print(a.message)
# print(b.message)

class Tweet: 
    def __init__(self, message):
        print('Hi')
        self.x = message
    
a = Tweet('soemthing here')
b = Tweet(' another one')