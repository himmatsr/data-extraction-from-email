from flask import Flask, jsonify, json, request
app = Flask(__name__)
import re
import nltk
import json
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import os
path_to_gs="C:\Program Files\gs\gs9.27\bin"
os.environ['PATH']+=os.pathsep+path_to_gs
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.tree import Tree
# load all the stopwords in english language in stop variable
stop = stopwords.words('english')
import requests
import json
import datetime
from datetime import date
def extract_phone_numbers(string):
    r = re.compile(r'(\d{3,4}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

@app.route("/post",methods = ['POST','GET'])
def gmail_addon():
    if request.method=='POST':

        # initialize a variable string which contain the content of email

        empty=[" "]
        data_ = request.get_json()
        string = data_["content"]
        # string ="""Dear Hema,



        #                        Please Ignore the previous mail .Kindly arrange two
        #             vehicles to the following warehouse by tomorrow as below.



        #             1.       17Ft vehicle from Rajankunte to Marathalli.

        #             2.       Tata Ace Mysore road (Chair & Sofa warehouse) to Marathalli.





        #         Thanks and Regards,

        #         Prem

        #         Featherlite Collections

        #         No.90/6, Marathahalli ORR, Munnekolalu,

        #         Bangalore  - 560037

        #     PH:080-42099068 / 42214168


        #     e. acctsm@featherlitefurniture.com
        #     """
        numbers = extract_phone_numbers(string)
        ne_tree = ne_chunk(pos_tag(word_tokenize(string)))
        # print("type(ne_tree[0] ",type(ne_tree[0]))
        sentence = word_tokenize(string)
        sentence_tag=pos_tag(sentence)
        # print("sentence tags are: ",sentence_tag)
        grammar1 = r"number_of_vehicles : {<CD>+<NNS>}"
        # number_of_vehicles = nltk.RegexpParser(grammar1)
        # chunk_no_of_vehicles = number_of_vehicles.parse(sentence_tag)
            # chunk_no_of_vehicles.draw()
        grammar2 = r"pickup_address : {<IN>+(<NNP>|<CD>)+}"
        PICKUP = nltk.RegexpParser(grammar2)
         # create a chunk tree for pickup locations
        chunk_PICKUP = PICKUP.parse(sentence_tag)
        # chunk_PICKUP.draw()
        grammar3 = r"drop_address : {<TO>+(<NNP>|<VB>|<NN>)+}"#removing <CD>
        DROP = nltk.RegexpParser(grammar3)
        chunk_DROP = DROP.parse(sentence_tag)
        # chunk_DROP.draw()
        drop_add = []
        # loop over the whole chunk_tree of chunk_Droplocations to find the loacations
        # which contain the subtree of drop_locations
        # also save that index into variable
        for i in range(len(chunk_DROP)):
            if type(chunk_DROP[i]) == nltk.tree.Tree:
                #print(chunk_DROP[i].label())
                loc_chunk = i
                
                if(chunk_DROP[i].label() == 'drop_address'):
                    temp= ""
                    for j in range(1,len(chunk_DROP[i].leaves())):
                        temp = temp + chunk_DROP[i].leaves()[j][0] + " "
                        # drop_add.append(chunk_DROP[i].leaves()[j][0])

                    drop_add.append(temp)

        for i in range(len(drop_add)):
            drop_add[i] = drop_add[i].strip(" ")
        final_drop=[];

        for i in drop_add:
            i=i.lower()
            final_drop.append(i)
        # print(final_drop)

        stringlower = string.lower()

        grammar4 = r'\bdost|bolero|tata\sace|tata\ssuper\sace|canter\s14|canter14|canter19|canter20|canter17|14ft|14\sft|canter\s17|17ft|17\sft|canter\s19|19ft|19\sft|20ft|20\sft|canter\s20|tata\s407|bolero|dost\b'
        vehicle_type= re.findall(grammar4,stringlower)
        # print(vehicle_type)
        dates=re.findall("(\d+/?-?\.\d+/?-?\.\d+)",string )
        # print(date)
        if len(dates)==0:
            today=date.today()
            today = today.strftime("%d/%m/%Y")
            if(stringlower.find("tomorrow")!=-1):
                tomorrow=datetime.date.today() + datetime.timedelta(days=1)
                tomorrow =tomorrow.strftime("%d/%m/%Y")
                dates.append(tomorrow)
            else:
                dates.append(today)
        # print(dates)

        vehicle_type= re.findall(grammar4,stringlower)
        final_vehicle=[]

        for i in range(len(vehicle_type)):
            if vehicle_type[i] =="14ft" or vehicle_type[i]=="14 ft":
                final_vehicle.append("canter 14")
            elif vehicle_type[i]=="17ft" or vehicle_type[i]=="17 ft":
                final_vehicle.append("canter 17")
            elif vehicle_type[i]=="19ft" or vehicle_type[i]=="19 ft":
                final_vehicle.append("canter 19")
            elif vehicle_type[i]=="20ft" or vehicle_type[i]=="20 ft":
                final_vehicle.append("canter 20")
            else:
                final_vehicle.append(vehicle_type[i])
        # print("final_vehicle",final_vehicle)      
        # print("vehicle type : ",vehicle_type)
        print("check for email string data", string)
        pickupString=string.replace('\r',' ')
        pickupString=pickupString.replace('\n',' ')
        print("Checking for email truncated", pickupString)
        pickupString=re.sub(' +', ' ',pickupString)
       
        pickupString=pickupString.lower()
        string_lower = pickupString
        # print(string_lower)
        Vehiclelist=['tata ace', 'tata super ace', 'canter 14', '14ft','14 ft', 'canter 17', '17ft','17 ft', 'canter 19', '19ft','19 ft','20 ft','20ft','tata 407','bolero','dost','canter14','canter17','canter19','canter20']
        for element in Vehiclelist:

            if element in pickupString:
                pickupString=pickupString.replace(element, 'word_to_be_replaced')

        findpickups=pickupString.split()
        index=0
        index_list=[]
        for word in findpickups:

            if word == 'word_to_be_replaced':
                index_list.append(index+len(word)+1)
                index=index+len(word)+1
            else:
                index=index+len(word)+1

        index_list_to=[]
        index=0;
        for i in index_list:
            index=pickupString.find('to',i)
            index_list_to.append(index)

        pick=[]
        for i in range(len(index_list)):
            pick.append(pickupString[index_list[i]:index_list_to[i]])

        final_pick=[]
        for i in pick:
            index=i.find('from')
            if index==-1:
                final_pick.append(i)
            else:
                s=i[index+5:]
                final_pick.append(s)

        for i in range(len(final_pick)):
            final_pick[i]=final_pick[i].strip()

        # print("final_pick",final_pick)

        vehicle_index =[]
        temp=0
        for element in vehicle_type:
            index= string_lower.find(element,temp)
            temp=index+len(element)
            vehicle_index.append(index)

        pickup_index = []
        temp=0
        for element in final_pick:
            index= string_lower.find(element,temp)
            temp=index+len(element)
        #     print(index)
            pickup_index.append(index)

        drop_index = []
        temp=0
        for element in final_drop:
            index= string_lower.find(element,temp)
            temp=index+len(element)
            drop_index.append(index)


        # print("drop index: ",drop_index)
        # print("pickup index: ", pickup_index)
        # print("vehicle index: ", vehicle_index)



        key=[]
        order={}

        i=0
        j=0
        k=0
        inner=[]
        print(final_pick)
        print(final_drop)
        print(final_vehicle)
        while k < len(drop_index):
            print("II",i)
            print("JJ",j)
            print("KK",k)
            print("LENGTH PICKUP",len(pickup_index))
            print("LENGTH DROP",len(drop_index))
            print("LENGTH VEHCILE",len(vehicle_index))
            while (i < len(vehicle_index) and vehicle_index[i] < pickup_index[j] ):
                inner.append(final_vehicle[i])
                i=i+1
            order["vehicle"]=inner
            inner =[]

            while j<len(pickup_index) and pickup_index[j]<drop_index[k]:
                inner.append(final_pick[j])
                j=j+1
            order["pickup"]=inner
            inner=[]
            if i==len(vehicle_index):
                while k<len(drop_index):
                    inner.append(final_drop[k])
                    k=k+1
            else:
                while k<len(drop_index) and drop_index[k]<vehicle_index[i]:
                    inner.append(final_drop[k])
                    k=k+1
            order["drop"]=inner
            inner=[]
            key.append(order)
        #     print(key)
            order={}
        # print(dir(date))
        
        print("check for value of JJJJ",j)

        d={}
        d["main"]=key

        d["date"]=dates
        if len(numbers)==0:
            d["mobile"]=empty
        else:
            d["mobile"]=numbers

        print(d)
        return jsonify(d)
    else:
     return "ERROR in Post Request"


if __name__ == "__main__":
    app.run()