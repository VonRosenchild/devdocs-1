# Plot the window and its frequency response:

from scipy import signal
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt

window = signal.slepian(51, width=0.3)
plt.plot(window)
plt.title("Slepian (DPSS) window (BW=0.3)")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

plt.figure()
A = fft(window, 2048) / (len(window)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))
response = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
plt.plot(freq, response)
plt.axis([-0.5, 0.5, -120, 0])
plt.title("Frequency response of the Slepian window (BW=0.3)")
plt.ylabel("Normalized magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")
