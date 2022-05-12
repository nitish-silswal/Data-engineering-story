import json
import copy
music_schema = {
    'Top Tracks':{
        'song-name':"",
        'is_local':"",
        "popularity":"",
        "ms_played":"",
        "application" : ""
    },
    'User Profile': {
        "Country":"",
        "application" : ""
    },
    'Top Artists':{
        "artist":"",
        "followers":0,
        "popularity":0,
        "application" : ""
    },
    'ODEN_ID':""
}



app_schema = {
    'Top Tracks':{
        'song-name':['top_tracks','items',[],'name'],
        'is_local':['top_tracks','items',[],'is_local'],
        "popularity":['top_tracks','items',[],'popularity'],
        "ms_played":['top_tracks','items',[],'duration_ms'],
        "application" : ""
    },
    'User Profile': {
        "Country":['user_profile','country'],
        "application" : ""
    },
    'Top Artists':{
        "artist":['top_artists','items',[],'name'],
        "followers":['top_artists','items',[],'followers','total'],
        "popularity":['top_artists','items',[],'popularity'],
        "application" : ""
    },
    'ODEN_ID':['oden_id']
}

###################################    DIFFERENT DOMAIN ######################################################
###############################################################################################################
social_schema = {

    "account_information" : {
        "name" : "",
        "email_address" : "",
        "gender" : "",
        "phone_number" : "",
        "primary_location" : {
            "items" : [
                {
                    "pincode" : ""
                }
            ]
        }
        
    },

    "advertisement" : {
        "items" : [
            {
                "advertiser_name" : "",
                "application" : ""
            }
        ]
    },

    "profile_updates" : {
        "items" : [ 
           {
               "timestamp"  : "",
               "application" : ""
           }
        ]
    },

    "location_history" : {
        "items" : [],
        "application" : ""
    },

    "your_search_history" : {
        "items" : [
            {
                "title" : "",
                "timestamp" : "",
                "application" : ""
            }
        ]
    },

    "account_login_activity" : {
        "items" : [
            {
                "application" : "",
                "timestamp" : ""
            }
        ]
    },

    "your_posts" : {
        "items" : [
            {
                "title" : "",
                "timestamp" : "",
                "application" : ""
            }
        ]
    },
    
    "friends" : {
        "items" : [
            {
                "name" : "",
                "timestamp" : "",
                "application" : ""
            }
        ]
    }  
}

###############  Schema for FACEBOOK ########################################### 
app_schema_fb = {

    "account_information" : {
        "name" :  ["profile_information" , "profile_v2" , "name" , "full_name"] ,
        "email_address" : ["profile_information", "profile_v2", "emails" ,  "emails" , [] , 0],
        "gender" : ["profile_information","profile_v2","gender","gender_option"],
        "phone_number" : ["profile_information" , "profile_v2" , "phone_numbers", [] ,0,  "phone_number"],
        "primary_location" : {
            "items" : [
                {
                    "pincode" : ["primary_location" , "primary_location_v2" , "zipcode" , [] , 0]
                }
            ]
        }
        
    },

    "advertisement" : {
        "items" : [
            {
                "advertiser_name" : ["advertisers_using_your_activity_or_information" , "custom_audiences_all_types_v2" , [] , "advertiser_name"],
                "application" : ""
            }
        ]
    },

    "profile_updates" : {
        "items" : [ 
           {
               "timestamp"  : ["profile_update_history" , "profile_updates_v2" , [] , "timestamp"],
               "application" : ""
           }
        ]
    },

    "location_history" : {
        "items" : ["account_activity" , "account_activity_v2" , [] , "city"],
        "application" : ""
    },

    "your_search_history" : {
        "items" : [
            {
                "title" : ["your_search_history" , "searches_v2" , [] , "title"],
                "timestamp" : ["your_search_history" , "searches_v2" , [] , "timestamp"],
                "application" : ""
            }
        ]
    },

    "account_login_activity" : {
        "items" : [
            {
                "timestamp" : ["logins_and_logouts" , "account_accesses_v2" , [] , "timestamp"],
                "application" : ""
            }
        ]
    },

    "your_posts" : {
        "items" : [
            {
                "title" : ["your_posts_1" , [] , "title"],
                "timestamp" : ["your_posts_1" , [] , "timestamp"],
                "application" : ""
            }
        ]
    },
    
    "friends" : {
        "items" : [
            {
                "name" : ["friends" , "friends_v2" , []  ,"name"],
                "timestamp" : ["friends" , "friends_v2" , [] , "timestamp"],
                "application" : ""
            }
        ]
    }

  
}


######### Schema for INSTAGRAM ##############################################

app_schema_insta = app_schema_insta = {

    "account_information" : {
        "name" : "NA",
        "email_address" : "NA",
        "gender" : "NA",
        "phone_number" : "NA",
        "primary_location" : {
            "items" : [
                {
                    "pincode" : "NA"
                }
            ]
        }
        
    },

    "advertisement" : {
        "items" : [
            {
                "advertiser_name" : ["advertisers_using_your_activity_or_information" , "ig_custom_audiences_all_types" , [] , "advertiser_name"],
                "application" : ""
            }
        ]
    },

    "profile_updates" : {
        "items" : [ 
           {
               "timestamp"  : ["profile_changes", "profile_profile_change" , [] , "string_map_data", "change date" , "timestamp"],
               "application" : ""
           }
        ]
    },

    "location_history" : {
        "items" : "NA",
        "application" : "NA"
    },

    "your_search_history" : {
        "items" : [
            {
                "title" : "NA",
                "timestamp" : "NA",
                "application" : "NA"
            }
        ]
    },

    "account_login_activity" : {
        "items" : [
            {
                "timestamp" : ["login_activity" , "account_history_login_history" , [] , "string_map_data" , "time" , "timestamp"],
                "application" : ""
            }
        ]
    },

    "your_posts" : {
        "items" : [
            {
                "title" : ["posts_1", [] , "title"],
                "timestamp" : ["posts_1", [] , "timestamp"],
                "application" : ""
            }
        ]
    },
    
    "friends" : {
        "items" : [
            {
                "name" : "NA",
                "timestamp" : "NA",
                "application" : "NA"
            }
        ]
    }  
}


########## Schema for SNAPCHAT ##############################################

app_schema_snap = {

    "account_information" : {
        "name" : "NA",
        "email_address" : "NA",
        "gender" : "NA",
        "phone_number" : "NA",
        "primary_location" : {
            "items" : [
                {
                    "pincode" : "NA"
                }
            ]
        }
        
    },

    "advertisement" : {
        "items" : [
            {
                "advertiser_name" : "NA",
                "application" : "NA"
            }
        ]
    },

    "profile_updates" : {
        "items" : [ 
           {
               "timestamp"  : "NA",
               "application" : "NA"
           }
        ]
    },

    "location_history" : {
        "items" : ["location_history" , "Location History" , [] , "City"],
        "application" : "NA"
    },

    "your_search_history" : {
        "items" : [
            {
                "title" : "NA",
                "timestamp" : "NA",
                "application" : "NA"
            }
        ]
    },

    "account_login_activity" : {
        "items" : [
            {
                "application" : ["account" , "Login History" , [] , "Created"],
                "timestamp" : ""
            }
        ]
    },

    "your_posts" : {
        "items" : [
            {
                "title" : "",
                "timestamp" : "",
                "application" : ""
            }
        ]
    },
    
    "friends" : {
        "items" : [
            {
                "name" : ["friends","Friends" , [] , "Display Name"],
                "timestamp" : ["friends","Friends" , [] , "Creation Timestamp"],
                "application" : ""
            }
        ]
    }  
}


##########################################                CODE           ###################################


def extractList(DSR, path) :
    if(len(path) == 0) :
        return DSR
    data = []
    for i in range(0,len(DSR)) :
        data.append(extractKeyFromDSR(DSR[i],path))
    return data



def extractKeyFromDSR(DSR,path) :
#     print('keyFromDSR')
    if(len(path) == 0) : 
        return ""
    obj = copy.deepcopy(DSR)
    for i in range(0,len(path)) :
        if(type(path[i])==type("abcd")) : # type matching with a string
            obj = obj[path[i]]
        elif(type(path[i]) == type([])) :
            print("path = " , path[i+1:])
            obj = extractList(obj, path[i+1:])
            break
    return obj



def extractSchemaFromDSR(DSR, meta_schema, app_schema , app_name) :
    data = {}
    for key in meta_schema.keys():
        if(str(type(meta_schema[key])) == '<class \'dict\'>') :
            data[key] = extractSchemaFromDSR(DSR,meta_schema[key],app_schema[key] , app_name)
        elif key == "application":
            data[key] = app_name
        else :
            data[key] = extractKeyFromDSR(DSR,app_schema[key])
    return data






# DSR = json.load(open('spotify_json.json'))
# data = extractSchemaFromDSR(DSR, music_schema, app_schema , "Spotify") 

# file = open("spot_out.json" , "w")
# json.dump(data , file , indent = 3)


DSR = json.load(open('fb_json.json'))
data = extractSchemaFromDSR(DSR, social_schema, app_schema_fb , "Facebook") 

file = open("fb_out.json" , "w")
json.dump(data , file , indent = 3)

# DSR = json.load(open('insta_json.json'))
# data = extractSchemaFromDSR(DSR, social_schema, app_schema_insta , "Instagram") 

# file = open("insta_out.json" , "w")
# json.dump(data , file , indent = 3)




