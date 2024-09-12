import os

def main():
    dir_path = "./"
    brainrot = 0
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            brainrot += 1
    bruh = open(f"vro{brainrot - 1}.txt", "w")
    bruh.write("lol")
    bruh.close()
    brainrot += 1
    pass

if __name__ == "__main__":
    main()