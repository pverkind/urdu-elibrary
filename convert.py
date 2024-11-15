from openiti.new_books.convert.epub_converter_UrduElib  import UrduElibEpubConverter
import os
import re

outfolder = r"D:\AKU\OpenITI\new\urdu-elibrary\converted"
if not os.path.exists(outfolder):
    os.makedirs(outfolder)

converter = UrduElibEpubConverter(dest_folder=outfolder)
converter.VERBOSE = False
#fp = r"epub/2897_Alf-Laila-wa-Laila_1.epub"
#converter.convert_file(fp)
for fn in os.listdir("epub"):
    #if "Laila-wa" in fn and fn.endswith("epub"):
    if fn.endswith("epub"):
        fp = os.path.join("epub", fn)
        print(fp)
        converter.convert_file(fp)

def combine_volumes(folder, common_title_str):
    combined_meta = ""
    combined_body = ""
    meta_splitter = "#META#Header#End#"
    filenames = [fn for fn in os.listdir(folder)\
                 if common_title_str in fn\
                 and fn.endswith("ARkdown")\
                 and "Vols" not in fn]
    filenames = sorted(filenames, key=lambda fn: fn.split("_")[-1].replace(".automARkdown", ""))

    for fn in filenames:
        print(fn)
        fp = os.path.join(folder, fn)
        with open(fp, mode="r", encoding="utf-8") as file:
            text = file.read()
        header, body = text.split(meta_splitter, maxsplit=1)
        magic_value, header = header.split("\n", maxsplit=1)
        combined_meta += header
        combined_body += body
    combined_fn = re.sub("_\d+.automARkdown", "", filenames[0])
    combined_fp = os.path.join(folder, combined_fn+"Vols")
    print(combined_fp)
    with open(combined_fp, mode="w", encoding="utf-8") as file:
        file.write(magic_value+combined_meta+meta_splitter+combined_body)

#folder = "converted"
#common_title_str = "Laila-wa"
#combine_volumes(folder, common_title_str)
        
