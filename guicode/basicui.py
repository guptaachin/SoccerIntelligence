import tkinter as tk
from guicode import http_request


def main():
    top = tk.Tk()
    top.geometry("500x500")

    query_button = tk.Button(top, text = "press me to shoot a query", command = fn_shoot_query)
    query_button.place(x = 200, y = 200)

    top.mainloop()


def fn_shoot_query():
    query = "PREFIX schema: <http://schema.org/> select ?person where { ?person schema:play_2018 ?s. } limit 5"
    response = http_request.make_request(query)
    do_something_with_this(response)


def do_something_with_this(response):
    print(response)


if __name__ == "__main__":
    main()
