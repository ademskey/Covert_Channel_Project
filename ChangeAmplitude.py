from pydub import AudioSegment


def ChangeAmplitude(filename, AmpShift, OutputFile):
    wav_file = AudioSegment.from_file(file=filename,
                                      format="wav")
    loud_wav_file = wav_file + AmpShift
    loud_wav_file.export(out_f=OutputFile,
                         format="wav",
                         bitrate="2000k",)
    return loud_wav_file


if __name__ == '__main__':
    # todo test main

    print('todo')
