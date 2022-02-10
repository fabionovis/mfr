import os
import argparse
import logging
import string

logging.basicConfig(level=logging.INFO)

def process(file_path):
    ''' This function does the main process
    '''
    assert file_path.endswith('.txt')
    assert os.path.isfile(file_path)
    
    logging.info('Opening the input file %s', file_path)
    
    with open(file_path) as input_file:
        data = input_file.read()
        
    logging.info('Done. Found a number of %d characters', len(data))
    
    '''Prepare a dictionary which contains each 
       character's frequency
    '''
    freq_dict = {key : 0 for key in string.ascii_lowercase}
    
    for ch in data.lower():
        freq_dict[ch] += 1
        
    norm = float(sum(freq_dict.values()))
    
    for ch in string_ascii_lowercase:
        freq_dict[ch]/=norm
        
    for ch, freq in freq_dict.items():
        print('{}: {:.3f}%'.format(ch, freq * 100.))
         
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help = 'path to the input file')
    
    args = parser.parse_args()
    process(args.infile)
