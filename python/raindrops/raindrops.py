def convert(number):
    raindrops = [v for k, v in {
        3: "Pling", 5: "Plang", 7: "Plong"}.items() if number % k == 0]
    return "".join(raindrops) if raindrops else str(number)
