import os 
import argparse
import json
import random
import numpy as np




from collections import defaultdict

# must break paths 
# finds file, shows the directory it is in and dirs in that directory 
# then enters that dir and finds the files in that dir 
# once dirs is empty, the connection is broken 
# if the the dirs do not contain files they will be empty 

def write_json(json_data):
    # write json file
    #print("--------\n", json_data)

    # convert dict to json string
    json_string = json.dumps(json_data)

    # write json string to file
    with open(args.output, 'w') as f:
        f.write(json_string)
        f.close()
    #print('done')

    return

def get_colors(object):
    
    # get random rgba color
    

    extension = object.split('.')[-1]
    if "." in object:
        #print("extension: ", extension)
    
        if extension in [n.split('.')[-1] for n in json_data['label']]:
            
            return colors_dict[extension]

        else: 
            random_color = list(np.random.choice(range(256), size=3))
            random_color.append(opacity)
            new_color = 'rgba({0},{1},{2},{3})'.format(random_color[0], random_color[1], random_color[2], random_color[3], opacity)
            colors_dict[extension] = new_color

            return new_color 
    else:
        #print("object: ", object)
        return 'rgba(255,255,255,0.8)'
            

def getFileInfo(root, file):
    #print("root: ", root)
    #print("file: ", file)
    filetype = os.popen('''file "{0}"'''.format(os.path.join(root,file))).read().split(':')[1].split(' ')[1]

    date = os.path.getmtime(os.path.join(root,file))
    filesize = os.path.getsize(os.path.join(root,file))
    #print("filesize: ", filesize)

    if filesize < 3: 
        filesize = 7

   
    return filetype, date, filesize



if __name__ == '__main__':
    opacity = 0.87
    colors = ['rgba(255,0,255,0.8)', 'rgba(255,0,255,0.)', 'rgba(255,0,255,0.4)', 'rgba(255,0,255,0.2)', 'rgba(255,0,255,0.0)']

    parser = argparse.ArgumentParser(description='Extract metadata from files in a directory and save to a JSON file')
    parser.add_argument('directory', help='Directory to search')
    parser.add_argument('output', help='Output JSON file')
    args = parser.parse_args()
    colors_dict = defaultdict(list)
    json_data = defaultdict(list)
    index = -1
    root_vals = []
    dires_dict = defaultdict(list)
    for root, dirs, files in os.walk(args.directory):
     
        index += 1
        json_data['label'].append(root)
        root_vals.append(index)
        dires_dict[root] = index
        # json_data['value'].append(1)

        # for dir in dirs:
            # index += 1
        #     buy = index -1
        #     json_data['label'].append(dir)
        #     json_data['source'].append(root_vals[-1])
        #     json_data['target'].append(index)
            # json_data['value'].append(1)
           
        for file in files:
            index += 1
            buy = index -1
            
            json_data['source'].append(root_vals[-1])
            json_data['target'].append(index)
            json_data['value'].append(getFileInfo(root, file)[2])
            json_data['color'].append(get_colors(file))
            json_data['label'].append(file)


    #print(dires_dict)


    for root, dirs, files in os.walk(args.directory):

        for dir in dirs: 
            if os.path.join(root, dir) in dires_dict:
                json_data['target'].append(dires_dict[os.path.join(root, dir)])
                json_data['source'].append(dires_dict[root])
                json_data['value'].append(1)
    
    json
    write_json(json_data)   

    
      
 

    





            
        
                


        
       

    




            
       




