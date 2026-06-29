class Palindrom_with_Exxtra_Memory:
    def valid_palindrom(self, message):
        x = []
        y = []
        is_palindrom = True
        for i, letter in enumerate(message):
            if letter.isalnum():
                x.append(letter.lower())
                y.append(letter.lower())
        for i in range(len(x)):
            if x[i] == y[-(i+1)]:
                continue
            else:
                is_palindrom = False
                is_palindrom
                break 
        return is_palindrom

    

class Palindrom:
    def valid_palindrom(self, message):
        left = 0
        right = len(message) - 1
        while left <= right:
            if message[left].isalnum() == False:
                left += 1
            elif message[right].isalnum() == False:
                right -= 1
            elif message[left].lower() == message[right].lower():
                left += 1
                right -= 1
            else:
                return False
            
        return True





x = Palindrom_with_Exxtra_Memory()
y = Palindrom()
string = "A man, A Plan, A CAnal: Panama"

# print(x.valid_palindrom(string))
print(y.valid_palindrom(string))

        






        





    


