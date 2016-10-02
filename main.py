from py4chan import py4chan

if __name__ == "__main__":

    while True:

        board = input("Entre with board name, example: sp\n")
        thread = input ("Entre with thread number:\n")

        c = py4chan(board,thread)
        c.verific_url()

        if c.Url != None:
            print ("-"*30)
            print (c)

            c.get_links_content()
            c.clear_Link()
            c.creat_dir()
            c.download_images()
            print(c.Links)

            print("GREAT\n"+"-"*30)
            q = input("Download another board? (y/n)\n")
            if q == "n":
                break;
        else:
            print ('Error, try again\n'+"-"*30)

