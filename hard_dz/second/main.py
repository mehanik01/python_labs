from pydub import AudioSegment

wav_file = AudioSegment.from_wav("Killer.wav")

def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


print('Замедлить или Ускорить?')
print('УСКОРЕНИЕ: (1.5; 2; 3 )  \nЗАМЕДЛЕНИЕ:( 0.5; 0.7, 0.8 )')

user_input = input('введите коэф:  ')

fast_sound = speed_change(wav_file, float(user_input))

fast_sound.export("output audio/новый трек3.wav", format="wav")