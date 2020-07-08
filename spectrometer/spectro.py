import numpy as np
import matplotlib.pyplot as plt
import cv2

# maximum intensity
imax = 255
wavelength_Range = 400
img = cv2.imread("spectra.jpg", 0)
pix_max = img.shape[1]
pix_max_f = wavelength_Range/pix_max
print(pix_max)
print(np.amax(img), np.amin(img))
spectra = np.mean(img, axis=0)
print(spectra)
wavelength = np.arange(400, 800, pix_max_f, dtype=float)
print(wavelength)

print(spectra.size, wavelength.size)

plt.subplot(211), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(212)
plt.plot(wavelength, spectra)
plt.xlabel("wavelength in nm")
plt.ylabel("Intensity")
plt.show()

