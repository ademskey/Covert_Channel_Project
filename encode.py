from shift_pitch import Shift_pitch
from Overlay import OverlayAudio
from ChangeAmplitude import ChangeAmplitude
from filter import high_pass
from pydub import AudioSegment
from pydub.playback import play


def main():
    source_file = 'dog.wav'
    carrier_file = 'rick.wav'
    frequency = 75
    sampling_rate = 88200*8
    amp_shift = 25

    source = AudioSegment.from_file(file=source_file,
                                    format="wav")
    play(source)

    shifted = Shift_pitch(
        source_file, 'pitch_shifted.wav', frequency=frequency)

    play(shifted)
    amp_down = ChangeAmplitude(
        'pitch_shifted.wav', -amp_shift, 'amp_shifted.wav')

    play(amp_down)

    overlay = OverlayAudio(carrier_file, 'amp_shifted.wav', False)

    play(overlay)

    overlay.export(out_f='encoded_overlay.wav',
                   format="wav",
                   bitrate="2000k",)

    high_pass('encoded_overlay.wav', 'filtered.wav')

    filtered = AudioSegment.from_file(file='filtered.wav',
                                      format="wav")
    play(filtered)

    restored = Shift_pitch(
        'filtered.wav', 'pitched_down.wav', frequency=-frequency)

    play(restored)

    amp_up = ChangeAmplitude('pitched_down.wav', amp_shift, 'decoded.wav')

    play(amp_up)


main()
