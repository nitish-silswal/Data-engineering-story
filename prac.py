import copy
import json
from decimal import Decimal


all_social_apps = ["Facebook" , "Instagram" , "Snapchat" , "Reddit", "Pinterest"]

fb_list = [
    [["account_information" , "name"],["profile_information" , "profile_v2" , "name" , "full_name"]],
    [["account_information" , "email_address"],["profile_information", "profile_v2", "emails" , "emails" , 0]],
    [["account_information","gender"],["profile_information","profile_v2","gender","gender_option"]],
    [["account_information" , "phone_number"],["profile_information" , "profile_v2" , "phone_numbers", 0 , "phone_number"]],
    [["account_information" , "primary_location" , "items"] , ["primary_location" , "primary_location_v2" , "zipcode"] , ["zipcode"]],
    [["advertisement" , "items"],["advertisers_using_your_activity_or_information" , "custom_audiences_all_types_v2"] , ["advertiser_name" , "application"]],
    [["profile_updates", "items"],["profile_update_history" , "profile_updates_v2"] , ["timestamp" , "title"]],
    [["location_history" , "items"] , ["account_activity" , "account_activity_v2"] , ["city" , "application"]],
    [["your_search_history" , "items"] , ["your_search_history" , "searches_v2"] , ["title" , "timestamp","application"]],
    [["account_login_activity" , "items"] , ["logins_and_logouts" , "account_accesses_v2"] , ["timestamp" , "application"]],
    [["your_posts" , "items"] , ["your_posts_1"] , ["title" , "timestamp" , "application"]],
    [["friends","items"] , ["friends" , "friends_v2"] , ["name" , "timestamp" , "application"]]
]


insta_list = [
    [["advertisement" , "items"] , ["advertisers_using_your_activity_or_information" , "ig_custom_audiences_all_types"] , ["advertiser_name" , "application"]],
    [["profile_updates" , "items"] , ["profile_changes", "profile_profile_change"] , ["string_map_data;change date;timestamp" , "application"]],
    [["account_login_activity" , "items"] , ["login_activity" , "account_history_login_history"] , ["string_map_data;time;timestamp" , "application"]],
    [["your_posts" , "items"] , ["posts_1"] , ["title","creation_timestamp","application"]]
]

snapchat_list = [
    [["account_login_activity" , "items"] , ["account" , "Login History"] , ["Created" , "application"]],
    [["friends" , "items"] , ["friends","Friends"] , ["Display Name" , "Creation Timestamp"]],
    [["location_history" , "items"] , ["location_history" , "Location History"] , ["City" , "application"]]
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
            extract_fields = app_list[curr_pos][2] # fields to plucked out from the app_dic (DSR json of current application)
            if len(social_dic[social_keys[-1]]):
                social_dic[social_keys[-1]].pop()  # remove the initial dummy data present in the social_dic (only put there for defining the format)
            for el in app_dic[app_keys[i]]:  
                obj = {}
                for elem in extract_fields:
                    if elem in el:                  # if elem is a key in both, extract the value and place directly
                        obj[elem] = el[elem]       
                    elif elem == "application":     # if elem is "application", simply place the name of the application as it is with "application" as the key
                        obj[elem] = app_name        
                    elif ";" in elem:               # split using ";" as a delimiter, and extract out the data from the last element of the nesting/list
                        temp_elem = copy.deepcopy(elem)
                        temp_el = copy.deepcopy(el)
                        temp_elem = temp_elem.split(";")
                        for temp_key in temp_elem:
                            temp_el = temp_el[temp_key]
                        obj[temp_elem[-1]] = temp_el

                    else: # field not present in the dic
                        obj[elem] = None
                social_dic[social_keys[-1]].append(obj)             
            return 
                                


# function to ensure data works after getting pulled from DynamoDB (helps prevent AWS related data format issues)
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



# fill data from Facebook DSR json into the Standard Social json blueprint/template
def fill_info_from_facebook(social_template_json , fb_json , fb_list):
    for i in range(len(fb_list)):
        nested_put(social_json_template , fb_json , fb_list , i , "Facebook")

# fill data from Instagram DSR json into the Standard Social json blueprint/template
def fill_info_from_instagram(social_template_json , insta_json , insta_list):
    for i in range(len(insta_list)):
        nested_put(social_json_template , insta_json , insta_list , i , "Instagram")

# fill data from Snapchat DSR json into the Standard Social json blueprint/template
def fill_info_from_snapchat(social_template_json , snapchat_json , snapchat_list):
    for i in range(len(snapchat_list)):
        nested_put(social_json_template , snapchat_json , snapchat_list , i , "Snapchat")



if __name__ == "__main__":
    social_json_template = json.load(open("social_json_template.json" , "r"))
    fb_json = json.load(open("fb_json.json" , "r"))
    fill_info_from_facebook(social_json_template , fb_json, fb_list)
    # out= open("output.json" , "w")
    # json.dump(social_json_template , out , indent = 2)


    # social_json_template = json.load(open("social_json_template.json" , "r"))
    insta_json = json.load(open("insta_json.json" , "r"))
    fill_info_from_instagram(social_json_template , insta_json, insta_list)
    # out= open("output.json" , "w")
    # json.dump(social_json_template , out , indent = 2)


    # social_json_template = json.load(open("social_json_template.json" , "r"))
    snapchat_json = json.load(open("snapchat_json.json" , "r"))
    fill_info_from_snapchat(social_json_template , snapchat_json, snapchat_list)
    out= open("output.json" , "w")
    json.dump(social_json_template , out , indent = 2)