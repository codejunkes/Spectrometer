import numpy as np
import matplotlib.pyplot as plt
import cv2

# maximum intensity
imax = 255
range = 400
img = cv2.imread("images/sarbo1.jpg", 0)
pix_max_w = img.shape[1]
pix_max_h = img.shape[0]
pix_max_f = range/pix_max_w
print(pix_max_w)
print(int(pix_max_h))
print(np.amax(img), np.amin(img))
spectra = np.mean(img, axis=0)
central = int(int(pix_max_h)/2)
central_spectra = img[:][central]
print("central spectrum size is: " + str(central_spectra.size) + "")
print(spectra)
wavelength = np.arange(400, 800, pix_max_f, dtype=float)
print(wavelength)

#print(spectra.size, wavelength.size)

plt.subplot(311), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(312)
plt.plot(wavelength, central_spectra)
plt.xlabel("wavelength in nm")
plt.ylabel("Intensity")
plt.subplot(313)
plt.plot(wavelength, spectra)
plt.xlabel("wavelength in nm")
plt.ylabel("Intensity")
plt.show()
