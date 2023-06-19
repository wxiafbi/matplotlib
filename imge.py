import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asanyarray(Image.open('./143593.jpg'))
print(repr(img))
print(len(img))
plt.imshow(img)
plt.plot([500, 600, 700], [500, 600, 700], marker='v', color='C99')

plt.show()
