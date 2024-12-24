#import libraries
import sounddevice as sd
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt

# Sampling frequency
freq = 10000

# Recording duration
duration = 5

# Start recorder with the given values of 
# duration and sample frequency
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)


Fs, data  = read("recording0.wav")

data = data[:, 0]
print("sampling frequency = ", Fs)

plt.subplot(3,1,1)
plt.plot(data)
plt.title('audio in time domain')
plt.xlabel('time t -->')
plt.ylabel('magnitude')

plt.subplot(3,1,2)
plt.magnitude_spectrum(data, Fs)
plt.title('Magnitude spectrum')

plt.subplot(3,1,3)
plt.phase_spectrum(data)
plt.title('Phase spectrum')

plt.show()



