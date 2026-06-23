import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker Version 1.0 Created by Ankit")
    while True:
        x = input("Enter what you want me to speak (or 'q' to quit): ")
        if x.lower() == 'q':
            break
        command = f"say {x}"
        os.system(command)
