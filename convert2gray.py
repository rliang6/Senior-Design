import imageio

def convert2gray(fname):
    fname = '';
    vid = imageio.get_reader(fname);
    fps = vid.get_meta_data()['fps'];

    writer = imageio.get_writer(fname, fps=fps);

    for image in vid:
        writer.append_data(image[:,:,1]);

    writer.close()
