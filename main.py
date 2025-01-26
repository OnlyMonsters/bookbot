import string
letterdic={}
letters=string.ascii_lowercase

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_string=text.lower()
    prelim=counter(lowered_string)
#    final=spacer(lowered_string)
    val_based_rev = {k: v for k, v in sorted(letterdic.items(), key=lambda item: item[1], reverse=True)}
    detail=wordout(val_based_rev)
    print(f"{num_words} words found in the document")
    print(detail)



def counter(lowered_string):
    for x in letters:
        letterdic[x]=lowered_string.count(x)
    return(letterdic)

#def spacer(lowered_string):
#   letterdic[" "]=lowered_string.count(" ")
#   return(letterdic)
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def wordout(letterdic):
    for x,y in letterdic.items():
        print (f"The '{x}' character was found {y} times")


    
main()