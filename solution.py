def get_planet_name(id):
    planet  = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus", 
        8: "Neptune"}
    return planet.get(id, "Invalid ID")
