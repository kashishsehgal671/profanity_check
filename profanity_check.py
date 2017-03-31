import urllib
def read_file():
    quotes = open("C:\detect_profanity\movie_quotes.txt")
    content_of_file = quotes.read()
    print(content_of_file)
    quotes.close()
    profanity_check(content_of_file)

def profanity_check(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print(" PROFANITY ALERT!!!" )
    elif "false" in output:
        print(" No profanity found")
    else:
        print(" Could not scan document properly")
        
read_file()   
