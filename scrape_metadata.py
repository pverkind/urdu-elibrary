import requests
import json
import time
import os
import random


def download_json_data(json_folder, first_category=1, last_category=28, display_n=100, overwrite=False):
    """Download the category json files."""
    if not os.path.exists(json_folder):
        os.makedirs(json_folder)
    #absent_ids = [4,5,6,7,8,9,24]
    
    for cat_id in range(first_category,last_category+1):
        outfp = os.path.join(json_folder, f"{cat_id:02d}.json")
        if not overwrite and os.path.exists(outfp):
            continue
        page = 1
        url = f"https://www.urdu-elibrary.com/api/Book/GetBookCategoryByPaging/{cat_id}/{display_n}/{page}/none/false/false"
        print(url)
        resp = requests.get(url)
        
        with open(outfp, mode="w", encoding="utf-8") as file:
            json.dump(resp.json(), file, indent=2, ensure_ascii=False)
        
        time.sleep(random.randint(2,5))

def get_multiple(book_d, main_key, sub_key):
    try:
        return " :: ".join([str(d[sub_key]) for d in book_d[main_key]])
    except:
        print("failed extracting", sub_key, "from", main_key)
        return ""

def get_key(book_d, key, default=""):
    try:
        return str(book_d[key])
    except:
        print("failed extracting", key)
        return default
    

def json2csv(json_folder, csv_fp, first_category=1, last_category=28, overwrite=False):
    """
    Join all the metadata from the category jsons into a single csv file.
    """
    csv_header = "ID\tauthor_ids\tauthor_names_en\tauthor_names_ur\tcategory_ids\tcategory_names_en\tcategory_names_ur\tepub_fn\ttitle_en\ttitle_ur\tpublished_year\tvolume\tisbn"
    cat_dict = dict()
    tsv_dict = dict()
    for cat_id in range(first_category,last_category+1):
        infp = os.path.join(json_folder, f"{cat_id:02d}.json")
        print(infp)
        with open(infp, mode="r", encoding="utf-8") as file:
            cat_data = json.load(file)
        for i, book_d in enumerate(cat_data["booksPaging"]):
            print("----")
            print("book", i)
            ID = get_key(book_d, "Id")
            author_ids = get_multiple(book_d, "Authors", "Id")
            author_names_en = get_multiple(book_d, "Authors", "Name")
            author_names_ur = get_multiple(book_d, "Authors", "Name_Urdu")
            category_ids = get_multiple(book_d, "Categories", "Id")
            category_names_en = get_multiple(book_d, "Categories", "Name")
            category_names_ur = get_multiple(book_d, "Categories", "Name_Urdu")
            epub_fn = get_multiple(book_d, "Media", "FileName")
            title_en = get_key(book_d, "Title")
            title_ur = get_key(book_d, "Title_Urdu")
            published_year= get_key(book_d, "PublishedYear")
            volume = get_key(book_d, "Volume")
            isbn = get_key(book_d, "ISBN")
            
            tsv_dict[ID] = "\t".join([ID, author_ids, author_names_en, author_names_ur, 
                                      category_ids, category_names_en, category_names_ur,
                                      epub_fn, title_en, title_ur,
                                      published_year, volume, isbn
                                      ])

            # collect metadata for the category data: 
            for d in book_d["Categories"]:
                if d["Id"] not in cat_dict:
                    cat_dict[d["Id"]] = d

    # store the csv file:
    with open(csv_fp, mode="w", encoding="utf-8") as file:
        file.write(csv_header)
        for ID,row  in sorted(tsv_dict.items()):
            file.write("\n"+row)

    # store the IDs and names of the categories: 
    cat_fp = os.path.join(json_folder, "categories.json")
    with open(cat_fp, mode="w", encoding="utf-8") as file:
        json.dump(cat_dict, file, indent=2, ensure_ascii=False, sort_keys=True)
    print(json.dumps(cat_dict, indent=2, ensure_ascii=False, sort_keys=True))
        

json_folder = "meta/json"
#download_json_data(json_folder, overwrite=False)
csv_fp = "meta/all_meta.csv"
json2csv(json_folder, csv_fp)
