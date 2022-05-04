from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
import json
from decimal import Decimal


fb_list = [
    [["account_information" , "name"],["profile_information" , "profile_v2" , "name" , "full_name"]],
    [["account_information" , "email_address"],["profile_information", "profile_v2", "emails" , "emails" , 0]],
    [["account_information","gender"],["profile_information","profile_v2","gender","gender_option"]],
    [["account_information" , "phone_number"],["profile_information" , "profile_v2" , "phone_numbers", 0 , "phone_number"]],
    [["advertisement" , "advertiser_names"],["advertisers_using_your_activity_or_information" , "custom_audiences_all_types_v2"] , ["advertiser_name"]]

]



def nested_get(dic, keys):
    for key in keys:
        dic = dic[key]
    return dic

def nested_put(social_dic, fb_dic , fb_list , curr_pos):
    social_keys = fb_list[curr_pos][0]
    fb_keys = fb_list[curr_pos][1]


    for i in range(len(social_keys) - 1):
        social_dic = social_dic[social_keys[i]]
    # simply a string type, place the extracted value
    if type(social_dic[social_keys[-1]]) == str:
        temp_dic = fb_dic
        social_dic[social_keys[-1]] = nested_get(temp_dic , fb_keys)
     # traverse the fb_dic internally till a list is encountered
    elif type(social_dic[social_keys[-1]]) == list:
        for i in range(len(fb_keys)):
            if type(fb_dic[fb_keys[i]]) != list:
                fb_dic = fb_dic[fb_keys[i]]
                continue

            #list encountered in fb_dic
            extract_fields = fb_list[curr_pos][2] # fields to plucked out from the fb_dic (fb DSR json)
            for el in fb_dic[fb_keys[i]]: 
                obj = {}
                for elem in extract_fields:
                    obj[elem] = el[elem]
                social_dic[social_keys[-1]].append(obj)             
            return 
                
                


def ReplaceDecimals(obj):
    if isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = ReplaceDecimals(obj[i])
        return obj
    elif isinstance(obj, dict):
        for k in obj.keys():
            obj[k] = ReplaceDecimals(obj[k])
        return obj
    elif isinstance(obj, Decimal):
        if obj % 1 == 0:
            return int(obj)
        else:
            return float(obj)
    else:
        return obj




def fill_info_from_facebook(social_template_json , fb_json , fb_list):
    for i in range(len(fb_list)):
        nested_put(social_json_template , fb_json , fb_list , i)


social_json_template = json.load(open("social_json_template.json" , "r"))
fb_json = json.load(open("fb_json.json" , "r"))
fill_info_from_facebook(social_json_template , fb_json, fb_list)
out= open("output.json" , "w")
json.dump(social_json_template , out , indent = 4)
