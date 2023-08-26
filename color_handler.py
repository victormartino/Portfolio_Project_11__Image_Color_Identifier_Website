HEX_DICT = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}


class ColorHandler:
    def __init__(self, colors):
        self.colors = colors
        self.colors_in_hex = []
        for rgb_color in self.colors:
            hex_calc = (
                (rgb_color[0] // 16), (rgb_color[0] % 16), (rgb_color[1] // 16), (rgb_color[1] % 16),
                (rgb_color[2] // 16),
                (rgb_color[2] % 16))
            color_values = []
            for color in hex_calc:
                hex_val = HEX_DICT[color]
                color_values.append(str(hex_val))
            final_hex_color = "".join(color_values)
            self.colors_in_hex.append(f'#{final_hex_color}')

    def get_hex_colors(self):
        return self.colors_in_hex
