import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

incoming_param = input()

while incoming_param.lower()!="exit":
    tokens = nltk.tokenize.word_tokenize(incoming_param)
    pos_tags = nltk.pos_tag(tokens)
    final_output = ""
    print(pos_tags)
    if len(pos_tags)==1:
        final_output = pos_tags[0][0]
    elif len(pos_tags)==2:
        if pos_tags[0][1]=="WRB":
            if pos_tags[1][1]=="NN":
                final_output = pos_tags[0][0]+" is the "+pos_tags[1][0]+"?"
            elif pos_tags[1][1]=="NNS":
                final_output = pos_tags[0][0]+" are the "+pos_tags[1][0]+"?"
        elif pos_tags[0][1]=="WP":
            if pos_tags[1][1]=="NN" or pos_tags[1][1]=="VBP":
                final_output = pos_tags[0][0]+" is that "+pos_tags[1][0]+"?"
            elif pos_tags[1][1]=="NNS" or pos_tags[1][1]=="VBD":
                final_output = pos_tags[0][0]+" are those "+pos_tags[1][0]+"?"
        elif pos_tags[0][1]=="NN" and (pos_tags[1][1]=="NN" or pos_tags[1][1]=="NNS"):
            final_output = pos_tags[0][0]+" is at the "+pos_tags[1][0]
        elif pos_tags[0][1]=="NNS" and (pos_tags[1][1]=="NN" or pos_tags[1][1]=="NNS"):
            final_output = pos_tags[0][0]+" are at the "+pos_tags[1][0]
        elif (pos_tags[0][1]=="RB" or pos_tags[0][1]=="VB") and (pos_tags[1][1]=="NN" or pos_tags[1][1]=="NNS"):
            final_output = pos_tags[0][0]+" to the "+pos_tags[1][0]
            
            
    elif len(pos_tags)==3:
        if pos_tags[0][1]=="WRB" and pos_tags[2][1][:2]=="VB":
            if pos_tags[1][1]=="NNS":
                final_output = pos_tags[0][0]+" do the "+pos_tags[1][0]+" "+pos_tags[2][0]+"?"
            elif pos_tags[1][1]=="NN":
                final_output = pos_tags[0][0]+" does the "+pos_tags[1][0]+" "+pos_tags[2][0]+"?"
        elif pos_tags[0][1]=="WRB" and pos_tags[1][1]=="JJ":
            if pos_tags[2][1]=="NN" or pos_tags[2][1]=="VBP":
                final_output = pos_tags[0][0]+" "+pos_tags[1][0]+" is that "+pos_tags[2][0]+"?"
            elif pos_tags[2][1]=="NNS" or pos_tags[2][1]=="VBD":
                final_output = pos_tags[0][0]+" "+pos_tags[1][0]+" are those "+pos_tags[2][0]+"?"
        elif pos_tags[0][1]=="NN" and pos_tags[1][1]=="RB" and pos_tags[2][1]=="NN":
            final_output = "The "+pos_tags[0][0]+" is "+pos_tags[1][0]+" to the "+pos_tags[2][0]
        elif pos_tags[0][1]=="NN" and pos_tags[1][1]=="JJ" and pos_tags[2][1]=="NN":
            final_output = "The "+pos_tags[0][0]+" is "+pos_tags[1][0]+" of the "+pos_tags[2][0]
        elif pos_tags[0][1]=="VB" and (pos_tags[1][1]=="NN" or pos_tags[1][1]=="JJ") and pos_tags[2][1]=="NN":
            final_output = pos_tags[0][0]+" "+pos_tags[1][0]+" to the "+pos_tags[2][0]
        elif pos_tags[0][1]=="WP" and pos_tags[1][1]=="NN" and pos_tags[2][1]=="NN":
            final_output = pos_tags[0][0]+" "+pos_tags[1][0]+" does the "+pos_tags[2][0]+" come"
    elif len(pos_tags)==4:
        if pos_tags[0][1]=="WP" and pos_tags[1][1]=="NN" and pos_tags[2][1]=="NN" and pos_tags[3][1]=="VB":
            final_output = pos_tags[0][0]+" "+pos_tags[1][0]+" does the "+pos_tags[2][0]+" "+pos_tags[3][0]

    if final_output == "":
        print("Currently does not support for complex sentences")
    else:
        print(final_output)
        
    
    incoming_param = input()
