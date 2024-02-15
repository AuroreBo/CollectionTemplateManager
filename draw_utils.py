from PIL import Image, ImageDraw

def draw_liked(image, liked: []):
    """ Draw ellispe at every liked pc position. """
    image = image.convert("RGB")
    draw = ImageDraw.Draw(image,"RGBA")
    print(f"nb of pc liked : {len(liked)}")
    for i in liked:
        # print(f"x{i.position[0]}, y {i.position[1]}, w {i.size[0]} ,h {i.size[1]}")
        x = i.position[0] + i.size[0] - 20
        y = i.position[1] + i.size[1] - 20
        # print(f"{x}, {y}")
        draw.ellipse((x, y, x+15, y+15), fill="#EDA2C0")

    return image

def draw_owned(image, owned: []):
    """ Draw faded rectangle at every owned pc position. """
    image = image.convert("RGB")
    draw = ImageDraw.Draw(image, "RGBA")
    print(f"nb of pc owned : {len(owned)}")
    for i in owned:
        x = i.position[0] - 2
        y = i.position[1] - 2
        w = i.position[0] + i.size[0] + 2
        h = i.position[1] + i.size[1] + 2
        # print(f"x{x}, y{y}, w{w}, h{h}")
        draw.rectangle((x, y, w, h), fill=(255, 255, 255, 204))

    return image

def draw_wanted(image, wanted: []):
    """ Draw rectangle border at every wanted pc position. """
    image = image.convert("RGB")
    draw = ImageDraw.Draw(image, "RGBA")
    print(f"nb of pc wanted : {len(wanted)}")
    for i in wanted:
        x = i.position[0] - 2
        y = i.position[1] - 2
        w = i.position[0] + i.size[0] + 2
        h = i.position[1] + i.size[1] + 2
        # print(f"x{x}, y{y}, w{w}, h{h}")
        draw.rectangle((x, y, w, h), fill=(0, 0, 0, 0), width=6, outline="#744FC6")

    return image
