import argparse

from __init__ import renderize_voice

ap = argparse.ArgumentParser()

ap.add_argument("-l", "--lyrics", required=True,
   help="Path to txt file containing the lyrics")
ap.add_argument("-m", "--midi", required=True,
   help="Path to midi file")
ap.add_argument("-g", "--gender", required=False, default="female", choices=['female', 'male'],
   help="Gender voice (female/male)")
ap.add_argument("-t", "--tempo", required=False, default=80,
   help="Song tempo in BPMs")
ap.add_argument("-d", "--destination_folder", required=False, default='.',
   help="Destination folder")
ap.add_argument("-method", "--method", required=False, default='1',
   help="metodo para cantar")
ap.add_argument("-lang", "--lang", required=False, default='es',
   help="idioma")
args = vars(ap.parse_args())

renderize_voice(args['lyrics'], args['midi'], args['gender'], int(args['tempo']), args['destination_folder'] ,int(args['method']) , args['lang'] ,"voice", "musica01.wav")



