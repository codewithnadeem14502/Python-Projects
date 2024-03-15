import json
filename = 'youtube.txt'
def load_data():
    try:
       with open(filename,'r') as file:
           return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(filename,'w') as file:
        #  dump (want write,where write)
         json.dump(videos,file)

def list_all_videos(vidoes):
    print('*'*50)
    print('*'*50)
    print("List of videos")
    print('*'*50)
    print('*'*50)
    print('\n')
    for index,video in enumerate(vidoes, start=1):
        print(f"{index}) Name : {video['name']}, Durartion: {video['time']}")

    print('\n')
    print('*'*50)  


def add_video(videos):
    name = input("Enter video name : ")
    time  = input("Enter video time : ")

    videos.append({"name":name,"time":time})

    save_data_helper(videos)
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the no of the video to updated : "))

    if 1 <= index <= len(videos):
         new_name = input("Enter new video name : ")
         new_time  = input("Enter new video time : ")
         print(videos[index-1],'has been updated successfully')
         print('\n')
         videos[index-1] = {'name':new_name, 'time':new_time}
         save_data_helper(videos)
    else:
        print("Invalid index selected")



def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of video to be deleted : "))
    
    if 1 <= index <= len(videos):
        print(videos[index-1],'has been deleted successfully')
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")
def main():
    videos = load_data()
    while True:
        print("\nYoutube Playlist Manager")
        print("1) List favorite videos")
        print("2) Add a YouTube video")
        print("3) Update a video")
        print("4) Delete a video")
        print("5) Exit the app")

        choice = input("Enter your choice: ")
        # print("vidoes : ")
        # print(videos)
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("\n Invalid choice, please try again") 



if __name__ == "__main__":
    main()
