def favorite_book(book="Das Kapital"):
    if book != "Das Kapital":
        formatted_string = "'"+ book[0].title()+book[1:] + "'"
    else:
        formatted_string = "'" + book + "'"
    print("Одна из моих самых любимых книг - это {}.".format(formatted_string))

    
favorite_book('Алиса в стране чудес')
favorite_book()


