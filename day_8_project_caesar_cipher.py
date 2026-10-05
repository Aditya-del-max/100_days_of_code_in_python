#Caesar cipher project
alphabets=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def cieser(plain_text, shift_text,direction):
    cipher_text=""
    if direction== "decode":
        shift_text*=-1
    for char in plain_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=position+ shift_text%26
            new_letter= alphabets[new_position]
            cipher_text+=new_letter
        else:
            cipher_text+=char
    print(f"The {direction}d text is {cipher_text} .")
should_continue=True
while should_continue:   
    answer=input("Type'encode' to encode or'decode' to decode ")
    word=list(input("enter the letter: ").upper())
    shift=int(input("enter digits to shift: "))
    cieser(plain_text=word,shift_text=shift,direction=answer)
    continues=input("do you want to continue ? ")
    if continues=="no":
        should_continue=False