# import required libraries 
from pydub import AudioSegment 
from pydub.playback import play 
from ChangeAmplitude import ChangeAmplitude
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

# Import an audio file 
# Format parameter only 
# for readability 



def OverlayAudio(Carrier, Hidden, recovery):
    wav_file = AudioSegment.from_file(file = Carrier, 
                                    format = "wav") 
    wav_file2 = AudioSegment.from_file(file = Hidden, 
                                    format = "wav") 

    if recovery == False:

        new_wav_file = wav_file.overlay(wav_file2)
        # Play the audio file 

        """new_wav_file.export(out_f="encoded.wav",
                    format="wav",
                    bitrate="2000k",)"""
    else:

        inverted = wav_file2.invert_phase()

        new_wav_file = wav_file.overlay(inverted)
        # Play the audio file 

        """new_wav_file.export(out_f="recovered.wav",
                    format="wav",
                    bitrate="2000k",)"""
        
    return new_wav_file




if __name__ == '__main__':
    
    File1 = 'Sample.wav'
    File2 = 'encoded_lib.wav'
    Original = AudioSegment.from_file(file = File2, 
                                    format = "wav") 

    OverlayAudio(File1, File2, 10000, False)
    OverlayAudio('encoded.wav', File1, 10000,  True)

    Reconstructed = AudioSegment.from_file(file =  'recovered.wav',
                                    format = "wav") 

    play(Original)
    play(Reconstructed)
