
import librosa
import soundfile
from pydub import AudioSegment
import soundfile as sf
from pydub.playback import play
import numpy as np


def Shift_pitch(filename, output_file, frequency):
    sampling_rate = 88200*8
    y, sr = librosa.load(filename, sr=sampling_rate)
    steps = frequency
    new_y = librosa.effects.pitch_shift(
        y, sr=sr, n_steps=steps, bins_per_octave=12, res_type='soxr_vhq')
    # print("HERE", np.max(new_y), np.min(new_y))
    soundfile.write(output_file, new_y, sampling_rate, subtype='FLOAT')
    export = AudioSegment.from_file(file=output_file, format="wav")
    """export.export(out_f=output_file,
                    format="wav",
                    bitrate="5000k")"""
    return export


if __name__ == '__main__':
    # play('dog.wav')

    Shift_pitch('dog.wav', 'encoded.wav', 6000)
    wav_file = AudioSegment.from_file(file="encoded.wav",
                                      format="wav")
    silent_wav_file = wav_file - 30
    silent_wav_file.export(out_f='encoded.wav',
                           format="wav",
                           bitrate="192k",)

    play(silent_wav_file)

    Shift_pitch('encoded.wav', 'decoded.wav', -6000)
    wav_file = AudioSegment.from_file(file="decoded.wav",
                                      format="wav")
    loud_wav_file = wav_file + 30
    loud_wav_file.export(out_f='decoded.wav',
                         format="wav",
                         bitrate="192k",)

    play(loud_wav_file)
    print('done')
