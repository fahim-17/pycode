# Mandelbrot fractal
# FB - 201003151
from PIL import Image
# drawing area (xa < xb and ya < yb)
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
maxIt = 256 # iterations
# image size
imgx = 128
imgy = 128
image = Image.new("RGB", (imgx, imgy),0)

for y in range(imgy):
    cy = y * (yb - ya) / (imgy - 1)  + ya
    for x in range(imgx):
        cx = x * (xb - xa) / (imgx - 1) + xa
        c = complex(cx, cy)
        z = 0
        for i in range(maxIt):
            if abs(z) > 2.0:
                r=0
                g=0
                b=0
                break
            z = z * z + c
            r = i % 4 * 64
            g = i % 8 * 32
            b = i % 16 * 16
            image.putpixel((x, y), b * 65536 + g * 256 + r)

image.save("d:\\mandel.png", "PNG")
