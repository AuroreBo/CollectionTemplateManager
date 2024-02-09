from PIL import Image, ImageDraw

def draw_liked(image, liked: []):
    draw = ImageDraw.Draw(image)
    print(f"nb of pc liked : {len(liked)}")
    for l in liked:
        x = l.position[0] + 5
        y = l.position[1] - 5
        print(f"{x}, {y}")
        draw.ellipse((x, y, x+15, y+15), fill="red")

    return image
def ellipse(output_path):
    image = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(image)
    draw.ellipse((25, 50, 175, 200), fill="red")
    draw.ellipse((100, 150, 275, 300), outline="black", width=5,
                 fill="yellow")

    image.save(output_path)