from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
import json
from decimal import Decimal


fb_list = [
    [["account_information" , "name"],["profile_information" , "profile_v2" , "name" , "full_name"]],
    [["account_information" , "email_address"],["profile_information", "profile_v2", "emails" , "emails" , 0]],
    [["account_information","gender"],["profile_information","profile_v2","gender","gender_option"]],
    [["account_information" , "phone_number"],["profile_information" , "profile_v2" , "phone_numbers", 0 , "phone_number"]],
    [["advertisement" , "advertiser_names"],["advertisers_using_your_activity_or_information" , "custom_audiences_all_types_v2"] , ["advertiser_name"]],
    [["profile_updates", "items"],["profile_update_history" , "profile_updates_v2"] , ["timestamp" , "title"]],
    [["location_history" , "items"] , ["account_activity" , "account_activity_v2"] , ["city"]],
    [["your_search_history" , "items"] , ["your_search_history" , "searches_v2"] , ["title" , "timestamp","application"]],
    [["account_login_activity" , "items"] , ["logins_and_logouts" , "account_accesses_v2"] , ["timestamp" , "application"]],
    [["your_posts" , "items"] , ["your_posts_1"] , ["title" , "timestamp" , "application"]],
    [["friends","items"] , ["friends" , "friends_v2"] , ["name" , "timestamp" , "application"]]
]



def nested_get(dic, keys):
    for key in keys:
        dic = dic[key]
    return dic

def nested_put(social_dic, app_dic , app_list , curr_pos , app_name):
    social_keys = app_list[curr_pos][0]
    app_keys = app_list[curr_pos][1]


    for i in range(len(social_keys) - 1):
        social_dic = social_dic[social_keys[i]]
    # simply a string type, place the extracted value
    if type(social_dic[social_keys[-1]]) == str:
        temp_dic = app_dic
        social_dic[social_keys[-1]] = nested_get(temp_dic , app_keys)
     # traverse the app_dic internally till a list is encountered
    elif type(social_dic[social_keys[-1]]) == list:
        for i in range(len(app_keys)):
            if type(app_dic[app_keys[i]]) != list:
                app_dic = app_dic[app_keys[i]]
                continue

            #list encountered in app_dic
            extract_fields = app_list[curr_pos][2] # fields to plucked out from the app_dic (fb DSR json)
            if len(social_dic[social_keys[-1]]):
                social_dic[social_keys[-1]].pop()
            for el in app_dic[app_keys[i]]: 
                obj = {}
                for elem in extract_fields:
                    if elem in el:
                        obj[elem] = el[elem]
                    elif elem == "application":
                        obj[elem] = app_name
                    else: # field not present in the dic
                        obj[elem] = None
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
        nested_put(social_json_template , fb_json , fb_list , i , "Facebook")


social_json_template = json.load(open("social_json_template.json" , "r"))
fb_json = json.load(open("fb_json.json" , "r"))
fill_info_from_facebook(social_json_template , fb_json, fb_list)
out= open("output.json" , "w")
json.dump(social_json_template , out , indent = 2)
