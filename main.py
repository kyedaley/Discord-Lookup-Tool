import requests
import time
import json

try:
    requests.get("https://www.toptal.com/developers/hastebin/")
except ConnectionError:
    print("No internet or error trying to send request!")

def main():
    command = str(input("Command: "))

    if command == "userlookup":
        print("Starting user lookup")
        print("Pre-warning: You need to insert your token for this, so it can achieve some data on user")
        token = str(input("Token MUST BE USER ACCOUNT: "))
        headers = {
            "authorization": token
        }
        userID = str(input("Insert user id: "))
        resp = requests.get(f"https://discord.com/api/v9/users/{userID}/profile?with_mutual_guilds=true", headers=headers)
        parms = resp.json()
        userId = parms["user"]["id"]
        username = parms["user"]["username"]
        discriminator = parms["user"]["discriminator"]
        bio = parms["user"]["bio"]
        connected_acc = parms["connected_accounts"]
        print("User ID : ", userId, "\nusername : ",  username, "\ntag : ", discriminator, "\nabout me : ", bio, "\nconnected accounts : ", connected_acc) 
        main()
        
    elif command == "serverlookup":
            print("starting server lookup bare with us")
            time.sleep(2)
            inv = str(input("Insert end part of link of discord server link: "))
            resp = requests.get(f"https://discord.com/api/v9/invites/{inv}?inputValue=https%3A%2F%2Fdiscord.gg%2FHZFCqK9X&with_counts=true&with_expiration=true")
            parms = resp.json() 
            code = str(parms["code"])
            expires_at = parms["expires_at"]
            serverID = parms["guild"]["id"]
            serverName = parms["guild"]["name"]
            features = parms["guild"]["features"]
            verification_level = parms["guild"]["verification_level"]
            inviterName = parms["inviter"]["username"]
            inviterDiscrim = parms["inviter"]["discriminator"]
            print("Code : ", code, "\nexpirers at : ", expires_at, "\nServer ID : ", serverID, "\nServer Name : ", serverName, "\nfeatures : ", features, "\nverification level : ", verification_level, "\ninviter name : ", inviterName, "\nInviter tag : ", inviterDiscrim)
            main()
            
    else:
        main()

main()
