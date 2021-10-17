import glob, os, json
import shutil

def find_latest_version(patch_folder, id):
    path = patch_folder + '/' + id + '.json'
    if not os.path.exists(path):
        i = 1
        while True:
            path = patch_folder + '/' + id + '_v' + str(i) + '.json'
            if not os.path.exists(path):
                i -= 1
                path = patch_folder + '/' + id + '_v' + str(i) + '.json'
                break
            else:
                i += 1
    return path


# categories or tags
group_by_field = "categories"
# comment, view, like, download
sort_by_field = "like" + "_count"
categories = {}
for patch_folder in glob.iglob(os.path.expanduser('~/Library/Application Support/.ZoiaLibraryApp/*'), recursive=False):
    if not os.path.isfile(patch_folder):  # filter dirs
        id = os.path.basename(patch_folder)
        if id.isnumeric():
            try:
                path = find_latest_version(patch_folder, id)
                filename, file_extension = os.path.splitext(os.path.basename(path))
                f = open(path, )
                data = json.load(f)
                f.close()
                print(id)
                for category in data[group_by_field]:
                    category_list = categories.get(category['name'], [])
                    data['bin_path'] = os.path.dirname(path) + '/' + filename + '.bin'
                    category_list.append((data[sort_by_field], data))
                    categories[category['name']] = category_list
            except Exception as e:
                print(e)

for category in categories:
    list = categories[category]
    sorted_list = sorted(list, key=lambda elem: -elem[0])

    for i, t in enumerate(sorted_list):
        folder = str(int(i / 64))
        id_in_folder = i % 64
        try:
            os.stat(category + '_' + folder)
        except:
            os.mkdir(category + '_' + folder)

        sortid, data = t
        shutil.copyfile(data['bin_path'],
                        './{}_{}/{:03}_zoia_{}_{}.bin'.format(category, folder, id_in_folder, sortid, data[
                            'title'].replace(' ', '_').replace('/', '_')))
