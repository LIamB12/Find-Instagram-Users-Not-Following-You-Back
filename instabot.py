import instaloader
import pandas as pd


# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
bot.login(user="your_account_name", passwd="your_password")

# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'profile_name')

# Retrieving the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]

# Retrieving the usernames of all followings
followings = [followee.username for followee in profile.get_followees()]


doesnt_follow = []

for i in followings:
    if i not in followers:
        doesnt_follow.append(i)

print(doesnt_follow)

