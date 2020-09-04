import os

#Enter your path to your heap folder that needs to be sorted
folder_track = ''
#Enter path where you want to see sorted things
image_folder = ''
video_folder = ''
books_folder = ''
music_folder = ''

#Remember: you can add any extension you want, I won't judge you <3

for filename in os.listdir(folder_track):
    extension = filename.split(".")
    #for photos
    if len(extension) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "png"):
        file = folder_track + "/" + filename
        new_path = image_folder + "/"  + filename
        os.rename(file, new_path)
    #for videos
    if len(extension) > 1 and (extension[1].lower() == "mp4"):
        file = folder_track + "/" + filename
        new_path = video_folder + "/" + filename
        os.rename(file, new_path)
    #for music
    if len(extension) > 1 and (extension[1].lower() == "mp3"):
        file = folder_track + "/" + filename
        new_path = music_folder + "/" + filename
        os.rename(file, new_path)
    #for books
    if len(extension) > 1 and (extension[1].lower() == "pdf" or extension[1].lower() == "djvu"):
        file = folder_track + "/"  + filename
        new_path = books_folder + "/"  + filename
        os.rename(file, new_path)
