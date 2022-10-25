import os 
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Sankey Graph Generator")
    parser.add_argument('directory', help='Directory to walk', required=True)

    args = parser.parse_args()
    directory_of_dirv = os.path.dirname(os.path.realpath(__file__))
    
    os.system(f"python3 {directory_of_dirv}/met-cap.py {args.directory}")
    os.system(f"python3 {directory_of_dirv}/sankey-graph.py")
   