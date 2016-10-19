from py4chan import Py4chan

if __name__ == "__main__":

    while True:

        board = input("Type Board, example: sp\n")
        thread = input ("Type thread number:\n")

        c = Py4chan(board,thread)
        c.verific_url()

        if c.Url != None:
            print ("-"*30)

            c.get_links_content()
            print (c)
            c.download_images()
            print(c.Links)

            print("GREAT\n"+"-"*30)
            q = input("Download another board? (y/n)\n")
            if q == "n":
                break;
        else:
            print ('Error, try again\n'+"-"*30)

