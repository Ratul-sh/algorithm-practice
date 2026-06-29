class Palindrom:
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

    


x = Palindrom()
string = "A man, A Plan, A CAnal: Panama"

print(x.valid_palindrom(string))

        






        





    


