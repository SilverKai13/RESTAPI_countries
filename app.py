from flask import Flask, jsonify,json,Response
from unidecode import unidecode
import codecs


application = Flask(__name__)

#i previously saved all that given data to capitals.txt file
capitals_dict={}
file = codecs.open('capitals.txt',encoding='utf-8',mode="r")
#reading that file and getting those countries and capitals to capitals_dict
for line in file:
        capitals_dict[line.split(',')[0]]=line.split(',')[1].strip()
file.close()
#creating one more array to fetch countries with out case sensitiveness
capitals_lowercase={unidecode(i).lower():i for i in capitals_dict.keys()}

#as told in the instructions file. Implemented post method
@application.route('/capital/<string:s>',methods=['GET'])
def capital(s):
        #returns country and capital as json if its in our file
        if(unidecode(s).lower() in capitals_lowercase.keys()):
                data={s:capitals_dict[capitals_lowercase[unidecode(s).lower()]]}
                json_string=json.dumps(data,ensure_ascii = False)
                response = Response(json_string,content_type="application/json; charset=utf-8" )
                return response
        #does this if invalid string is given
        else:
                data={s:"Urgh! Darling, This country name Doesnt seem to exist on my programmer's map"}
                json_string=json.dumps(data,ensure_ascii = False)
                response = Response(json_string,content_type="application/json; charset=utf-8" )
                return response

if __name__=='__main__':
        application.run(host='0.0.0.0',debug=True)