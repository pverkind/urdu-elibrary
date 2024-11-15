# urdu-elibrary

This repository contains Urdu books converted into mARkdown format from the website urdu-elibrary.com

This library contains a number of epub books in Urdu. 

The metadata of the converted books can be found here: 
https://docs.google.com/spreadsheets/d/1FA4d7FBcXSENs30jJN8P1o42lumRdUPZnhQ-vuDWhJ8/edit?usp=sharing 

The converted books are found in the "converted" folder. 

## Categories: 
1 [Poetry](https://www.urdu-elibrary.com/showall/1)
2 [Fiction](https://www.urdu-elibrary.com/showall/2)
3 [Non-Fiction](https://www.urdu-elibrary.com/showall/3)
10 [Research and Criticism](https://www.urdu-elibrary.com/showall/10)
11 [Language and Linguistics](https://www.urdu-elibrary.com/showall/11)
12 [Kulliyyat](https://www.urdu-elibrary.com/showall/12)
13 [Biography](https://www.urdu-elibrary.com/showall/13)
14 [Journalism](https://www.urdu-elibrary.com/showall/14)
15 [Sociology and Religion](https://www.urdu-elibrary.com/showall/15)
16 [History](https://www.urdu-elibrary.com/showall/16)
17 [Education and Teaching](https://www.urdu-elibrary.com/showall/17)
18 [Science, Technology and Geography](https://www.urdu-elibrary.com/showall/18)
19 [Political Science](https://www.urdu-elibrary.com/showall/19)
20 [Medicine and Therapies](https://www.urdu-elibrary.com/showall/20)
21 [Philosopy](https://www.urdu-elibrary.com/showall/21)
22 [Fine Arts](https://www.urdu-elibrary.com/showall/22)
23 [Laws](https://www.urdu-elibrary.com/showall/23)
25 [Economics and Business](https://www.urdu-elibrary.com/showall/25)
26 [Library Science, Bibliographies & General Knowledge](https://www.urdu-elibrary.com/showall/26)
27 [Encyclopaedia and Dictionary](https://www.urdu-elibrary.com/showall/27)
28 [Children Literature](https://www.urdu-elibrary.com/showall/28)

NB: categories nos. 4-9 and 24 are not defined - their pages are empty, without even a heading

All books can be accessed through this link: https://www.urdu-elibrary.com/Books/showallcategory

## Downloading an epub from urdu-elibrary

The page contains an ePub reader, and downloads the entire epub.
The epub filename is <internal_ID>.epub
You have to be logged in to access the reader, but the internal ID of the book
is exposed on the book page in the filename of the cover page image 
(https://www.urdu-elibrary.com/Images/BookPhotos/<internal_ID>.jpg)
and also in the "Media" dictionary of the category API output (see below)

The book can then be downloaded using this URL:
https://www.urdu-elibrary.com/EncryptedBooks/EPubBooks/<internal_ID>.epub



## category API: 

The book metadata, sorted by category, can be extracted using the API: 

https://www.urdu-elibrary.com/api/Book/GetBookCategoryByPaging/<cat_no>/<number_of_items_to_display>/<page_no_1_based>/none/false/false

Returns json in the following format: 
{
    "TotalBooksCount": int,
    "TotalPage": int,
    "booksPaging": [
        {
            "Authors": [
                "Books": [], # other books by the same author??
                "Id": int, # numeric ID of the author
                "Name": str, # English name
                "Name_Urdu": str,
                "Name_Hindi": str
            ],
            "Cart": [],   # irrelevant
            "Categories": [ # list of categories to which the book belongs
                "Id": int,
                "Name": str, # name of the category in English
                "Name_Urdu": str,
                "Name_Hindi": str,
                "ModifiedOn": str
            ], 
            "Media": [
                "Id": int,
                "FileName": str, # <internal_book_id>.epub
                "IsSample": bool,
                "Book_id": int   # same as "Id"
            ],
            "Photos": [], 
            "Users": [],
            "Id": int,
            "Title": str, # title in English
            "Title_Urdu": str,
            "Title_Hindi": str,
            "Language": str,
            "ISBN": str,
            "Description": str, # description in English
            "Description_Urdu": str,
            "Description_Hindi": str,
            "Price": float,
            "isActive": bool, # true / false
            "PublishedDate": "YYY-MM-DDThh:mm:ss.hhh",
            "PublishedYear": str,
            "CreatedOn": "YYY-MM-DDThh:mm:ss.hhh",
            "ModifiedOn": "YYY-MM-DDThh:mm:ss.hhh",
            "Volume": str

        }
    ]
}