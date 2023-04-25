#Decipehering a message using a shifted alphabet cipher

import string

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
alphabet = "abcdefghijklmnopqrstuvwxyz"

#to decode a simple shift cipher
def decode(message,shift):
    for punctuation in string.punctuation:
        message = message.replace(punctuation, '')
    words = message.split(" ")
    deciphered_message_words = []
    for word in words:
        new_word = ""
        for letter in word:
            index = alphabet.find(letter)
            new_word = new_word + alphabet[(index+shift)%26]
        deciphered_message_words.append(new_word)

    deciphered_message = " ".join(deciphered_message_words)
    #print(deciphered_message)
    return deciphered_message

print(decode(message,10))

#to encode plain text with a simple shift cipher
def encode(plain_text,shift):
    for punctuation in string.punctuation:
        plain_text = plain_text.replace(punctuation, '')
    words = plain_text.split(" ")
    encoded_words = []
    for word in words:
        new_word = ""
        for letter in word:
            index = alphabet.find(letter)
            new_word = new_word + alphabet[(index-shift)%26]
        encoded_words.append(new_word)
    encoded_message = " ".join(encoded_words)
    return encoded_message  

print(encode(alphabet,-10))

#new messages below
message1 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
message2 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

print(decode(message1,10)) #tells us to change the shift in the decoding function 
print(decode(message2,14))

message3 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
for shift in range(0,25):
    print(decode(message3,shift))
  
#Vigenère Cipher below 

