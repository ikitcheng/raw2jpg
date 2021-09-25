import argparse
import rawpy
import imageio
import glob
from tqdm import tqdm

def raw2jpg_command():
    parser = argparse.ArgumentParser(description = "Convert .raw to .jpg")
    parser.add_argument("--inpath", '-i', required=True, help = "Path to folder containing .raw pictures", type=str)
    parser.add_argument("--outpath", '-o', default=None, help = "Default output is the same folder as the input.", type=str)
    args = parser.parse_args()

    batch_convert(args.inpath, args.outpath)


def raw2jpg(filename, outpath):

    with rawpy.imread(filename) as raw:
        rgb = raw.postprocess()
    if outpath is not None:
        # saw .jpg in outpath
        imageio.imsave(outpath + filename.split('\\')[-1][:-4]+'.jpg', rgb)
    else:
        # save .jpg in the same folder as the raw images
        imageio.imsave(filename[:-4]+'.jpg', rgb)


def batch_convert(path_to_imgs, outpath):
    filenames = glob.glob(f'{path_to_imgs}*.ARW')
    for f in tqdm(filenames):
        raw2jpg(f, outpath)
    print('Complete!')


if __name__ == '__main__':
    raw2jpg_command()