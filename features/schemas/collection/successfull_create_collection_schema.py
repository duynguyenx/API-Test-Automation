SUCCESSFUL_CREATE_COLLECTION_SCHEMA = {
 "definitions": {},
 "$schema": "http://json-schema.org/draft-07/schema#",
 "$id": "http://example.com/root.json",
 "type": "object",
 "title": "The Root Schema",
 "required": [
   "id",
   "title",
   "description",
   "published_at",
   "updated_at",
   "curated",
   "featured",
   "total_photos",
   "private",
   "share_key",
   "tags",
   "links",
   "user",
   "cover_photo",
   "preview_photos"
 ],
 "properties": {
   "id": {
     "$id": "#/properties/id",
     "type": "integer",
     "title": "The Id Schema",
     "default": 0,
     "examples": [
       4860865
     ]
   },
   "title": {
     "$id": "#/properties/title",
     "type": "string",
     "title": "The Title Schema",
     "default": "",
     "examples": [
       "123123123"
     ],
     "pattern": "^(.*)$"
   },
   "description": {
     "$id": "#/properties/description",
     "type": "string",
     "title": "The Description Schema",
     "default": "",
     "examples": [
       "Duy test 123123123"
     ],
     "pattern": "^(.*)$"
   },
   "published_at": {
     "$id": "#/properties/published_at",
     "type": "string",
     "title": "The Published_at Schema",
     "default": "",
     "examples": [
       "2019-05-22T05:46:32-04:00"
     ],
     "pattern": "^(.*)$"
   },
   "updated_at": {
     "$id": "#/properties/updated_at",
     "type": "string",
     "title": "The Updated_at Schema",
     "default": "",
     "examples": [
       "2019-05-22T05:46:32-04:00"
     ],
     "pattern": "^(.*)$"
   },
   "curated": {
     "$id": "#/properties/curated",
     "type": "boolean",
     "title": "The Curated Schema",
     "default": False,
     "examples": [
       False
     ]
   },
   "featured": {
     "$id": "#/properties/featured",
     "type": "boolean",
     "title": "The Featured Schema",
     "default": False,
     "examples": [
       False
     ]
   },
   "total_photos": {
     "$id": "#/properties/total_photos",
     "type": "integer",
     "title": "The Total_photos Schema",
     "default": 0,
     "examples": [
       0
     ]
   },
   "private": {
     "$id": "#/properties/private",
     "type": "boolean",
     "title": "The Private Schema",
     "default": False,
     "examples": [
       True
     ]
   },
   "share_key": {
     "$id": "#/properties/share_key",
     "type": "string",
     "title": "The Share_key Schema",
     "default": "",
     "examples": [
       "87bdaf74a488a8d38521f691cef24562"
     ],
     "pattern": "^(.*)$"
   },
   "tags": {
     "$id": "#/properties/tags",
     "type": "array",
     "title": "The Tags Schema"
   },
   "links": {
     "$id": "#/properties/links",
     "type": "object",
     "title": "The Links Schema",
     "required": [
       "self",
       "html",
       "photos",
       "related"
     ],
     "properties": {
       "self": {
         "$id": "#/properties/links/properties/self",
         "type": "string",
         "title": "The Self Schema",
         "default": "",
         "examples": [
           "https://api.unsplash.com/collections/4860865"
         ],
         "pattern": "^(.*)$"
       },
       "html": {
         "$id": "#/properties/links/properties/html",
         "type": "string",
         "title": "The Html Schema",
         "default": "",
         "examples": [
           "https://unsplash.com/collections/4860865/123123123"
         ],
         "pattern": "^(.*)$"
       },
       "photos": {
         "$id": "#/properties/links/properties/photos",
         "type": "string",
         "title": "The Photos Schema",
         "default": "",
         "examples": [
           "https://api.unsplash.com/collections/4860865/photos"
         ],
         "pattern": "^(.*)$"
       },
       "related": {
         "$id": "#/properties/links/properties/related",
         "type": "string",
         "title": "The Related Schema",
         "default": "",
         "examples": [
           "https://api.unsplash.com/collections/4860865/related"
         ],
         "pattern": "^(.*)$"
       }
     }
   },
   "user": {
     "$id": "#/properties/user",
     "type": "object",
     "title": "The User Schema",
     "required": [
       "id",
       "updated_at",
       "username",
       "name",
       "first_name",
       "last_name",
       "twitter_username",
       "portfolio_url",
       "bio",
       "location",
       "links",
       "profile_image",
       "instagram_username",
       "total_collections",
       "total_likes",
       "total_photos",
       "accepted_tos"
     ],
     "properties": {
       "id": {
         "$id": "#/properties/user/properties/id",
         "type": "string",
         "title": "The Id Schema",
         "default": "",
         "examples": [
           "kJ9efp45qkU"
         ],
         "pattern": "^(.*)$"
       },
       "updated_at": {
         "$id": "#/properties/user/properties/updated_at",
         "type": "string",
         "title": "The Updated_at Schema",
         "default": "",
         "examples": [
           "2019-05-22T05:46:32-04:00"
         ],
         "pattern": "^(.*)$"
       },
       "username": {
         "$id": "#/properties/user/properties/username",
         "type": "string",
         "title": "The Username Schema",
         "default": "",
         "examples": [
           "duynguyenhvn"
         ],
         "pattern": "^(.*)$"
       },
       "name": {
         "$id": "#/properties/user/properties/name",
         "type": "string",
         "title": "The Name Schema",
         "default": "",
         "examples": [
           "Duy Nguyen"
         ],
         "pattern": "^(.*)$"
       },
       "first_name": {
         "$id": "#/properties/user/properties/first_name",
         "type": "string",
         "title": "The First_name Schema",
         "default": "",
         "examples": [
           "Duy"
         ],
         "pattern": "^(.*)$"
       },
       "last_name": {
         "$id": "#/properties/user/properties/last_name",
         "type": "string",
         "title": "The Last_name Schema",
         "default": "",
         "examples": [
           "Nguyen"
         ],
         "pattern": "^(.*)$"
       },
       "twitter_username": {
         "$id": "#/properties/user/properties/twitter_username",
         "type": "null",
         "title": "The Twitter_username Schema",
         "default": "null",
         "examples": [
           "null"
         ]
       },
       "portfolio_url": {
         "$id": "#/properties/user/properties/portfolio_url",
         "type": "null",
         "title": "The Portfolio_url Schema",
         "default": "null",
         "examples": [
           "null"
         ]
       },
       "bio": {
         "$id": "#/properties/user/properties/bio",
         "type": "null",
         "title": "The Bio Schema",
         "default": "null",
         "examples": [
           "null"
         ]
       },
       "location": {
         "$id": "#/properties/user/properties/location",
         "type": "string",
         "title": "The Location Schema",
         "default": "",
         "examples": [
           "Viet Nam"
         ],
         "pattern": "^(.*)$"
       },
       "links": {
         "$id": "#/properties/user/properties/links",
         "type": "object",
         "title": "The Links Schema",
         "required": [
           "self",
           "html",
           "photos",
           "likes",
           "portfolio",
           "following",
           "followers"
         ],
         "properties": {
           "self": {
             "$id": "#/properties/user/properties/links/properties/self",
             "type": "string",
             "title": "The Self Schema",
             "default": "",
             "examples": [
               "https://api.unsplash.com/users/duynguyenhvn"
             ],
             "pattern": "^(.*)$"
           },
           "html": {
             "$id": "#/properties/user/properties/links/properties/html",
             "type": "string",
             "title": "The Html Schema",
             "default": "",
             "examples": [
               "https://unsplash.com/@duynguyenhvn"
             ],
             "pattern": "^(.*)$"
           },
           "photos": {
             "$id": "#/properties/user/properties/links/properties/photos",
             "type": "string",
             "title": "The Photos Schema",
             "default": "",
             "examples": [
               "https://api.unsplash.com/users/duynguyenhvn/photos"
             ],
             "pattern": "^(.*)$"
           },
           "likes": {
             "$id": "#/properties/user/properties/links/properties/likes",
             "type": "string",
             "title": "The Likes Schema",
             "default": "",
             "examples": [
               "https://api.unsplash.com/users/duynguyenhvn/likes"
             ],
             "pattern": "^(.*)$"
           },
           "portfolio": {
             "$id": "#/properties/user/properties/links/properties/portfolio",
             "type": "string",
             "title": "The Portfolio Schema",
             "default": "",
             "examples": [
               "https://api.unsplash.com/users/duynguyenhvn/portfolio"
             ],
             "pattern": "^(.*)$"
           },
           "following": {
             "$id": "#/properties/user/properties/links/properties/following",
             "type": "string",
             "title": "The Following Schema",
             "default": "",
             "examples": [
               "https://api.unsplash.com/users/duynguyenhvn/following"
             ],
             "pattern": "^(.*)$"
           },
           "followers": {
             "$id": "#/properties/user/properties/links/properties/followers",
             "type": "string",
             "title": "The Followers Schema",
             "default": "",
             "examples": [
               "https://api.unsplash.com/users/duynguyenhvn/followers"
             ],
             "pattern": "^(.*)$"
           }
         }
       },
       "profile_image": {
         "$id": "#/properties/user/properties/profile_image",
         "type": "object",
         "title": "The Profile_image Schema",
         "required": [
           "small",
           "medium",
           "large"
         ],
         "properties": {
           "small": {
             "$id": "#/properties/user/properties/profile_image/properties/small",
             "type": "string",
             "title": "The Small Schema",
             "default": "",
             "examples": [
               "https://images.unsplash.com/profile-1555670159112-744b402c0572?ixlib=rb-1.2.1&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=32&w=32"
             ],
             "pattern": "^(.*)$"
           },
           "medium": {
             "$id": "#/properties/user/properties/profile_image/properties/medium",
             "type": "string",
             "title": "The Medium Schema",
             "default": "",
             "examples": [
               "https://images.unsplash.com/profile-1555670159112-744b402c0572?ixlib=rb-1.2.1&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=64&w=64"
             ],
             "pattern": "^(.*)$"
           },
           "large": {
             "$id": "#/properties/user/properties/profile_image/properties/large",
             "type": "string",
             "title": "The Large Schema",
             "default": "",
             "examples": [
               "https://images.unsplash.com/profile-1555670159112-744b402c0572?ixlib=rb-1.2.1&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=128&w=128"
             ],
             "pattern": "^(.*)$"
           }
         }
       },
       "instagram_username": {
         "$id": "#/properties/user/properties/instagram_username",
         "type": "null",
         "title": "The Instagram_username Schema",
         "default": "null",
         "examples": [
           "null"
         ]
       },
       "total_collections": {
         "$id": "#/properties/user/properties/total_collections",
         "type": "integer",
         "title": "The Total_collections Schema",
         "default": 0,
         "examples": [
           18
         ]
       },
       "total_likes": {
         "$id": "#/properties/user/properties/total_likes",
         "type": "integer",
         "title": "The Total_likes Schema",
         "default": 0,
         "examples": [
           0
         ]
       },
       "total_photos": {
         "$id": "#/properties/user/properties/total_photos",
         "type": "integer",
         "title": "The Total_photos Schema",
         "default": 0,
         "examples": [
           0
         ]
       },
       "accepted_tos": {
         "$id": "#/properties/user/properties/accepted_tos",
         "type": "boolean",
         "title": "The Accepted_tos Schema",
         "default": False,
         "examples": [
           True
         ]
       }
     }
   },
   "cover_photo": {
     "$id": "#/properties/cover_photo",
     "type": "null",
     "title": "The Cover_photo Schema",
     "default": "null",
     "examples": [
       "null"
     ]
   },
   "preview_photos": {
     "$id": "#/properties/preview_photos",
     "type": "null",
     "title": "The Preview_photos Schema",
     "default": "null",
     "examples": [
       "null"
     ]
   }
 }
}