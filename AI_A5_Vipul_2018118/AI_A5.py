import nltk
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer
import string
import re
import inflect
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize   
import pickle
from num2words import num2words
lem=WordNetLemmatizer()

def user_answers(answer):
    temp=[]
    input1=input(answer)
    input1=input1.lower()
    input1=input1.translate(str.maketrans(" "," ",string.punctuation))
    final_tokens=[]
    input1= input1.split(" ")
    for tokens in input1:
        if(tokens.isdecimal()==True):
            tokens=num2words(tokens)
        word=lem.lemmatize(tokens)
        final_tokens.append(word)
    return final_tokens
file1 = open("E:/sem 7/AI/AI_A5_Vipul_2018118/facts.txt", 'w')


ans=user_answers("What kind of work you like? \n 1. Physical \n 2. Logical \n" )

if "logical" in ans:
    file1.write("physical_or_mental(mental).\n")
    ans1=user_answers("Having high aptitute skills? \n 1. Yes \n 2. No \n" ) 
    if "yes" in ans1:
        file1.write("aptitute(yes).\n")
        ans2=user_answers("Do you like technology or non-tech things? \n 1. Technical \n 2. Non-tech \n" ) 
        if "technical" in ans2:
            file1.write("tech_or_nontech(tech). \n")
            ans2=user_answers("Which exam you cleared? \n 1. CAT \n 2. GATE \n 3. GRE \n 4. None \n" )
            if "cat" in ans2:
                file1.write("given_exam(cat). \n")
            elif "gate" in ans2:
                file1.write("given_exam(gate). \n")
            elif "gre" in ans2:
                file1.write("given_exam(gre). \n")
            elif "none" in ans2:
                file1.write("given_exam(none). \n")
                ans3=user_answers("Do you like programming? \n 1. Yes \n 2. No \n")
                if "yes" in ans3:
                    file1.write("coding(yes). \n")
                else:
                    file1.write("coding(no). \n")
        else:
            file1.write("tech_or_nontech(nontech). \n")
            ans41=user_answers("do you have interest in doing business? \n 1. Yes 2. No \n")
            if "yes" in ans41:
                file1.write("business_oriented(yes). \n")
            else:
                file1.write("business_oriented(no). \n")
                ans4= user_answers(" Do you like to travel? \n 1. Traveller \n 2. Non-Traveller \n")
                if "traveller" in ans4:
                    file1.write("traveller_nontraveller(traveller). \n")
                    ans5= user_answers(" Do you like creativity and innovation? \n 1. Yes \n 2. No \n")
                    if "yes" in ans5:
                        file1.write("creative_and_innovative(yes). \n")
                else:
                    file1.write("traveller_nontraveller(nontraveller). \n")
                    ans5= user_answers(" Are you a person of creative and innovative ideas? \n 1. Yes \n 2. No \n")
                    if "yes" in ans5:
                        file1.write("creative_and_innovative(yes). \n")
    else:
        file1.write("aptitute(no). \n")
        ans6=user_answers("Do you like technology or non-tech things? \n 1. Technical \n 2. Non-tech \n" ) 
        if "technical" in ans6:
            file1.write("tech_or_nontech(tech). \n")
            ans7= user_answers(" Do you like to travel? \n 1. Traveller \n 2. Non-Traveller ")
            if "traveller" in ans7:
                    file1.write("traveller_nontraveller(traveller). \n")
                    ans8= user_answers(" Are you a person of creative and innovative ideas? \n 1. Yes \n 2. No \n")
                    if "yes" in ans8:
                        file1.write("creative_and_innovative(yes). \n")
            else:
                    file1.write("traveller_nontraveller(nontraveller). \n")
                    ans9= user_answers(" Are you a person of creative and innovative ideas? \n 1. Yes \n 2. No \n")
                    if "yes" in ans9:
                        file1.write("creative_and_innovative(yes). \n")
        else:
            file1.write("tech_or_nontech(nontech). \n")
            ans10= user_answers(" Do you like to travel? \n 1. Traveller \n 2. Non-Traveller ")
            if "traveller" in ans10:
                    file1.write("traveller_nontraveller(traveller). \n")
                    ans11= user_answers(" Are you a person of creative and innovative ideas? \n 1. Yes \n 2. No \n")
                    if "yes" in ans11:
                        file1.write("creative_and_innovative(yes). \n")
            else:
                    file1.write("traveller_nontraveller(nontraveller). \n")
                    ans12= user_answers(" Are you a person of creative and innovative ideas? \n 1. Yes \n 2. No \n")
                    if "yes" in ans12:
                        file1.write("creative_and_innovative(yes). \n")

elif "physical" in ans:
    file1.write("physical_or_mental(physical).\n")
    ans1=user_answers("Do you have leadership skills? \n 1. Yes \n 2. No \n" )
    if "yes" in ans1:
        file1.write("leadership(yes).\n")
        ans2=user_answers("Do you like taking risk? \n 1. Yes \n 2. No \n" )
        if "yes" in ans2:
            file1.write("risk_taker(yes). \n")
            ans3=user_answers("Having high aptitute skills? \n 1. Yes \n 2. No \n" )
            if "yes" in ans3:
                file1.write("aptitute(yes).\n")
        
                
        
    
print("Your facts are successfully saved in facts.txt file. \n Now you can use prolog for advicing career")

file1.close()




