from termcolor import colored

def sync(database):
    for bookx in database[0]['data']["books"]:
        for pubx in database[0]['data']["publishers"]:
            if bookx["publisher_id"] == pubx["id"]:
                bookx["publisher"] = pubx

    for user in database[0]['data']["users"]:
        for x in user["books_borrowed_ids"]:
            book_id = x
            user_id = user["lib_id"]
            for j in database[0]['data']["books_borrowed"]:
                if j["lib_id"] == user_id:
                    for book in database[0]['data']["books"]:
                        if book["id"] == book_id:
                            user["books_borrowed"].append(book)



def color_text(text,color):
    print(colored(f"{text}", f"{color}"))
