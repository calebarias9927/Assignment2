# Data for the Sandwich Maker Machine

# Recipes for different sizes of sandwiches
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slices
            "ham": 4,    # slices
            "cheese": 4, # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slices
            "ham": 6,    # slices
            "cheese": 8, # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slices
            "ham": 8,    # slices
            "cheese": 12, # ounces
        },
        "cost": 5.50,
    }
}

# Available resources in the machine
resources = {
    "bread": 12,  # slices
    "ham": 18,    # slices
    "cheese": 24, # ounces
}
