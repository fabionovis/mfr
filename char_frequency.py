import os
import argparse
import logging
import string

logging.basicConfig(level=logging.INFO)

def process(file_path, hist=False, order=False):
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
        if ch in string.ascii_lowercase:
            freq_dict[ch] += 1
            
    if hist:
        from matplotlib import pyplot as plt
        if not order:
            plt.bar(list(freq_dict.keys()), freq_dict.values())
        else:
            sorted_freq_dict = {k:v for k, v in sorted(freq_dict.items(), key = lambda item: item[1])}
            plt.bar(list(sorted_freq_dict.keys()), sorted_freq_dict.values(), log = True)
        plt.show()
        
    norm = float(sum(freq_dict.values()))
    
    for ch in string.ascii_lowercase:
        freq_dict[ch]/=norm
        
    for ch, freq in freq_dict.items():
        print('{}: {:.3f}%'.format(ch, freq * 100.))
        
    
         
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help = 'path to the input file')
    parser.add_argument('--histo', help = 'Plot the histogram of the relative frequency of each character', action = 'store_true')
    parser.add_argument('--order', help = 'Plot the histogram with the entries in increasing order', action = 'store_true')
        
    args = parser.parse_args()
    process(args.infile, args.histo, args.order)
    
