"""
to do:
1. list how many episodes watched out of total on select prompt.
"""
import random
import os

if os.path.exists("{0}\\cartoons.txt".format(os.getcwd())) != True:
    file = open("{0}\\cartoons.txt".format(os.getcwd()), "w")
    file.close()

watched = []
episodes = 0
seasons = 0
watching = ""
def new():
    while True:
        choice = input("Would you like to add a new cartoon to the list?(Y/N) ")
        if choice.lower() == "y" or choice.lower() == "yes":
            file = open("{0}\\cartoons.txt".format(os.getcwd()), "r")
            contents = []
            for line in file:
                if line.endswith("\n"):
                    line = line[0:len(line) - 1]
                contents.append(line)
            file.close()
            newc = input("Enter cartoon name: ")
            while True:
                seasons = input("How many seasons does the show have? ")
                try:
                    seasons = int(seasons)
                except ValueError:
                    print("{0} isn't a number".format(episodes))
                    continue
                while True:
                    episodes = input("How many episodes on average does each season have? ")
                    try:
                        episodes = int(episodes)
                        break
                    except ValueError:
                        print("{0} isn't a number".format(episodes))
                        continue
                break
            seasons = str(seasons)
            episodes = str(episodes)
            if int(episodes) < 10:
                episodes = "0" + episodes
            if int(seasons) < 10:
                seasons = "0" + seasons
            file = open("{0}\\cartoons.txt".format(os.getcwd()), "w")
            for i in contents:
                file.write(i + "\n")
            file.write(newc + "/{0} {1}".format(seasons, episodes))
            file.close()
            file = open("{0}\\{1}.txt".format(os.getcwd(), newc), "w")
            file.close()
            break
        elif choice.lower() == "n" or choice.lower() == "no":
            break
        else:
            print("{0} isn't a valid option".format(choice))
            continue
    pick()

def pick():
    global watched
    global episodes
    global seasons
    global watching
    options = []
    watched = []
    while True:
        num = 0
        file = open("{0}\\cartoons.txt".format(os.getcwd()), "r")
        print("Pick a cartoon")
        for line in file:
            if line.endswith("\n"):
                line = line[0:len(line) - 1]
            print("{0}: {1}".format(str(num + 1), line[0:len(line) - 6]))
            options.append(line)
            num += 1
        file.close()
        cartoon = input(": ")
        try:
            cartoon = int(cartoon)
        except (ValueError, TypeError):
            print("{0} isn't a number".format(cartoon))
            continue
        if cartoon > num:
            print("Please pick a number between 1 and {0}".format(num))
        else:
            break
    watching = options[cartoon - 1][0:len(options[cartoon - 1]) - 6]
    seasons = options[cartoon - 1][options[cartoon - 1].index("/") + 1:options[cartoon - 1].index("/") + 3]
    episodes = options[cartoon - 1][options[cartoon - 1].index("/") + 4:options[cartoon - 1].index("/") + 6]
    for i in options:
        options[options.index(i)] = options[options.index(i)][0:len(i) - 6]
    file = open("{0}\\{1}.txt".format(os.getcwd(), options[cartoon - 1]), "r")
    for line in file:
        watched.append(line)
    file.close()
    for i in watched:
        if i.endswith("\n"):
            watched[watched.index(i)] = i[0:len(i) - 1]
    main()

def main():
    global seasons
    global episodes
    global watched
    global watching
    season = random.randint(1, int(seasons))
    episode = random.randint(1, int(episodes))
    combo = str(season) + " " + str(episode)
    if len(watched) != int(seasons)*int(episodes):
        try:
            if combo not in watched:
                print("Season {0} Episode {1}".format(str(season), str(episode)))
                watched.append(combo)
                contents = []
                file = open("{0}\\{1}.txt".format(os.getcwd(), watching), "r")
                for line in file:
                    if line.endswith("\n"):
                        line = line[0:len(line) - 1]
                    contents.append(line)
                file.close()
                file = open("{0}\\{1}.txt".format(os.getcwd(), watching), "w")
                for i in contents:
                    file.write(i + "\n")
                file.write(combo + "\n")
                file.close()
            else:
                print("already generated {0}".format(combo))
                main()
            if len(watched) != int(seasons) * int(episodes):
                while True:
                    choice = input("y to generate another, n to pick new cartoon, nw to see how many episodes you watched, x to exit: ")
                    if choice.lower() == "y":
                        main()
                    elif choice.lower() == "n":
                        pick()
                    elif choice.lower() == "x":
                        exit()
                    elif choice.lower() == "nw":
                        print("You have watched {0}/{1} episodes".format(len(watched), str(int(seasons) * int(episodes))))
                        continue
                    else:
                        print("{0} is not a valid option".format(choice))
                        continue
            else:
                main()
        except RecursionError:
            main()
    else:
        print("You watched all of the show :D")
        while True:
            choice = input("n to pick new cartoon, nw to see how many episodes you watched, x to exit: ")
            if choice.lower() == "n":
                pick()
            elif choice.lower() == "nw":
                print("You have watched {0}/{1} episodes".format(len(watched), str(int(seasons) * int(episodes))))
                continue
            elif choice.lower() == "x":
                exit()
            else:
                print("{0} is not a valid option".format(choice))
                continue

new()