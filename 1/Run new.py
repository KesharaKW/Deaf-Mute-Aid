import serial
import pickle
import numpy as np
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

dict = {1:"School", 2:"Temple", 3:"Station", 4:"Why", 5:"Run", 6:"Turn", 7:"Left", 8:"Right", 9:"Water",
         10:"Time", 11:"Bus", 12:"Mountain", 13:"Dog", 14:"Play", 15:"Where", 16:"Hello", 17:"Bank", 18:"Shop", 19:"Train", 20:"Food", 21:"Hospital", 22:"Doctor",
         23:"Telephone", 24:"No", 25:"North", 26:"South", 27:"Bridge", 28:"When", 29:"Who"}
file = open('knnpickle_file', 'rb')
model = pickle.load(file)

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=6)
    ser.reset_input_buffer()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            all_words_in_sentence = []
            
            line = "195 117 18 1178 146 195 117 18 1178 146"
            serial_in = line.strip().split()
            serial_in = [int(i) for i in serial_in]
            for i in range(len(serial_in)//5):
                data = serial_in[i*5:(i*5)+5]
                print(data)
                data = np.array(data).reshape(1, 5)
                result = model.predict(data)
                word = None
                try:
                    word = dict_(result)
                    all_words_in_sentence.append(word)
                except:
                    print("No matching word for", end=": ")
                    print(data)

            incoming_param = " ".join(all_words_in_sentence)
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

            



