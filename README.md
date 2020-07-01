# 👻 GhostPost 👻

The GhostPost Machine™ is a website where people can anonymously post Boasts or Roasts of whatever they want. Like most services, there is a character limit: 280 characters.

Create a Django application with the following features:

## Back end:

-   One model to represent both boasts and roasts
    -   **BooleanField** to tell whether it's a boast or a roast
    -   **CharField** to put the content of the post in
    -   **IntegerField** for up votes
    -   **IntegerField** for down votes
    -   **DateTimeField** for submission time

## Fron end:

-   A homepage that displays boasts and roasts, sorted by time submitted
-   Buttons to filter the content by either boast or roasts, sorted by time submitted
-   Up votes and down votes buttons for each boast and roast
    -   When clicked, these buttons affect the number on the relevant post appropriately
-   Ability to sort content based on vote score
-   Page to submit a boast or a roast
-   Add a post deletion method that works for both boasts and roasts on the detail page.
    When a boast or a roast is created, it should have a random 6 character string associated with it. Every post now has two URLS... but one is public and one is private:
    -   `localhost:8000/posts/1`
    -   `localhost:8000/posts/abcdef`
-   The one that ends in an ID should display a _public_ version of the detail page and the one that ends in the _secret key_ should be the same content but with an additional button that allows you to delete the content

## installation

1. Use the package manager [poetry](https://python-poetry.org/) to start a virtual environment:

```bash
    poetry shell
```

2. Then, install all the dependencies required for this project:

```bash
    poetry install
```

3. Run the respective migrations:

```bash
    python manage.py migrate
```

4. Finally, run the server with the following command:

```bash
    python manage.py runserver
```
