import instaloader

# Create Instaloader object
loader = instaloader.Instaloader()

# Instagram username
username = input("Enter Instagram username: ")

try:
    # Download profile picture, posts, stories, etc.
    loader.download_profile(username, profile_pic_only=True)

    print(f"\nProfile '{username}' downloaded successfully!")

except Exception as e:
    print("Error:", e)