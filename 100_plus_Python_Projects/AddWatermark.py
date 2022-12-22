import os
from PIL import Image, ImageDraw, ImageFont


def get_position(img_width, img_height, text_width, text_height, position_id=9, margin=10):
    """
    get position by position id
    :param img_width:
    :param img_height:
    :param text_width:
    :param text_height:
    :param position_id:
    :param margin: text position margin value to the image
    :return: text position tuple
    """
    margin = 10
    if position_id == 1:
        return (margin, margin)
    elif position_id == 2:
        return img_width // 2 - text_width // 2, margin
    elif position_id == 3:
        return img_width - text_width - margin, margin
    elif position_id == 4:
        return margin, img_height // 2 - text_height // 2
    elif position_id == 5:
        return img_width // 2 - text_width // 2, img_height // 2 - text_height // 2
    elif position_id == 6:
        return img_width - text_width - margin, img_height // 2 - text_height // 2
    elif position_id == 7:
        return margin, img_height - text_height - margin
    elif position_id == 8:
        return img_width // 2 - text_width // 2, img_height - text_height - margin
    elif position_id == 9:
        return img_width - text_width - margin, img_height - text_height - margin


def add_watermark(filename, text, font_name='Roboto-Italic.ttf', font_size=20, font_opacity=50, position_id=9):
    """
    add watermark function
    :param filename:
    :param text:
    :param font_name:
    :param font_size:
    :param font_opacity:
    :param position_id: default right bottom 9
    :return:
    """
    # get image
    with Image.open(filename).convert("RGBA") as base:
        # create a blank image
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype(font_name, font_size)
        d = ImageDraw.Draw(txt)
        # get text width and height
        text_width, text_height = d.textsize(text, font=fnt)
        pos = get_position(base.size[0], base.size[1], text_width, text_height, position_id=position_id)
        # draw text with opacity
        d.text(pos, text, font=fnt, fill=(255, 255, 255, 256 * font_opacity // 100))
        out = Image.alpha_composite(base, txt)

        # save
        out_filename = 'watermark/{}'.format(os.path.basename(filename))
        if not os.path.exists('watermark'):
            os.makedirs('watermark')
        out.save(out_filename, 'PNG')


if __name__ == '__main__':
    text = input('Please input a watermark text : ').strip()
    font_size = int(input('Please input the font size: [20]') or '50')
    font_opacity = int(input('Please input the font opacity: [50]') or '50')
    position_id = int(input('Please input the position: [9]') or '9')

    for f in os.listdir('images'):
        if f.endswith('.png'):
            filename = 'images/{}'.format(f)
            print('add watermark for {}'.format(filename))
            add_watermark(filename=filename, text=text, font_size=font_size, font_opacity=font_opacity,
                          position_id=position_id)