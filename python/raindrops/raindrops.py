def convert(number):
    raindrops = [sound for factor, sound in {
        3: "Pling", 5: "Plang", 7: "Plong"}.items() if number % factor == 0]
    return "".join(raindrops) if raindrops else str(number)
