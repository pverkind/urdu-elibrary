import os
import requests
import csv
import time
import random
import re

def download_file(url, filepath):
    """
    Write the download to file in chunks,
    so that the download does not fill up the memory.
    See http://stackoverflow.com/a/16696317/4045481
    """
    r = requests.get(url, stream=True)
    with open(filepath, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)    

def download_books(meta_csv_fp, outfolder, ids=None, categories=None):
    if ids:
        ids = set([str(id_) for id_ in ids])
    if categories:
        categories = set([str(c) for c in categories])
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)
    base_url = "https://www.urdu-elibrary.com/EncryptedBooks/EPubBooks/"
    with open(meta_csv_fp, mode="r", encoding="utf-8") as file:
        for i, row in enumerate(csv.DictReader(file, delimiter="\t")):
            print(i)
            if categories:
                ignore = True
                for cat in row["category_ids"].split(" :: "):
                    if cat in categories:
                        ignore = False
                        break
                if ignore:
                    continue
            if ids and row["ID"] not in ids:
                continue
            if row["epub_fn"]:
                title = re.sub("\W+", "-", row["title_en"])
                if row["volume"]:
                    volume = "-".join(re.findall("\d+", row["volume"]))
                    outfn = f'{row["ID"]}_{title}_{volume}.epub'
                else:
                    outfn = f'{row["ID"]}_{title}.epub'
                outfp = os.path.join(outfolder, outfn)
                url = base_url + row["epub_fn"]
                print(url)
                print(">", outfn)
                if not os.path.exists(outfp):
                    download_file(url, outfp)
                    sleep_time = random.randint(5,15)
                    print("sleeping", sleep_time, "seconds")
                    time.sleep(sleep_time)
                    
            
            
meta_csv_fp = "meta/all_meta.csv"
outfolder = "epub"
#download_books(meta_csv_fp, outfolder, ids=[2897,2896,2894,2900,2901,2912], categories=[2])
download_books(meta_csv_fp, outfolder)
