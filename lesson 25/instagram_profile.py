
    import urllib.request
import json

def get_instagram_profile(username):
    url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode()
            json_data = json.loads(data)
            
            user = json_data.get('graphql', {}).get('user', {})
            if not user:
                print("User  not found or profile is private.")
                return
            
            profile_info = {
                "Username": user.get('username'),
                "Full Name": user.get('full_name'),
                "Biography": user.get('biography'),
                "Followers": user.get('edge_followed_by', {}).get('count'),
                "Following": user.get('edge_follow', {}).get('count'),
                "Posts": user.get('edge_owner_to_timeline_media', {}).get('count'),
                "Is Private": user.get('is_private'),
                "Is Verified": user.get('is_verified'),
                "Profile Pic URL": user.get('profile_pic_url_hd')
            }
            
            for key, value in profile_info.items():
                print(f"{key}: {value}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_username = input("Enter the Instagram username: ").strip()
    get_instagram_profile(target_username)
# This script fetches and displays basic profile information of a public Instagram user.# This script fetches and displays basic profile information of a public Instagram user.