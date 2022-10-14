# Gabe Harmston
# barebones ray tracer
import ray
from vec3 import Color
from vec3 import Vec3
from vec3 import Point3


def hit_sphere(center, radius, ray):
    # return boolean if ray intersects a sphere
    oc = ray.origin - center
    a = ray.direction.dot(ray.direction)
    b = 2.0 * ray.direction.dot(oc)
    c = oc.dot(oc) - radius * radius
    discriminant = b * b - 4 * a * c
    return discriminant >= 0


def ray_color(ray):
    # return color at pixel
    if hit_sphere(Point3(0, 0, -1), 0.5, ray):
        return Color(1, 1, 0)
    unit_direction = ray.direction.unit_vector()
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - t) * Color(1.0, 1.0, 1.0) + t * Color(0.5, 0.7, 1.0)


if __name__ == "__main__":

    # Image
    aspect_ratio = 16.0 / 9.0
    image_width = 600
    image_height = int(image_width / aspect_ratio)

    # Camera

    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    origin = Point3(0, 0, 0)
    horizontal = Vec3(viewport_width, 0, 0)
    vertical = Vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal / 2 - vertical / 2 - Vec3(0, 0, focal_length)

    # Render

    outfile = open("barebones.ppm", "w")
    outfile.write("P3\n")
    outfile.write(str(image_width) + " " + str(image_height) + "\n")
    outfile.write("255\n")

    for j in reversed(range(image_height - 1)):
        print("\rLines remaining: " + str(j))
        for i in range(image_width):
            u = float(i) / (image_width - 1)
            v = float(j) / (image_height - 1)
            r = ray.ray(origin, lower_left_corner + u * horizontal + v * vertical - origin)
            pixel_color = ray_color(r)
            color_x = int(pixel_color.x * 255)
            color_y = int(pixel_color.y * 255)
            color_z = int(pixel_color.z * 255)
            outfile.write(str(color_x) + " " + str(color_y) + " " + str(color_z) + " ")
    outfile.write("\n")
    outfile.close()
